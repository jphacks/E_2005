from flask import Flask, request, abort
from bot import app, db
from bot.models import User, Status

from linebot import (
    LineBotApi,
    WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, FollowEvent, JoinEvent,
    TextSendMessage
)
import os

#環境変数取得
LINE_CHANNEL_ACCESS_TOKEN = os.environ["LINE_CHANNEL_ACCESS_TOKEN"]
LINE_CHANNEL_SECRET = os.environ["LINE_CHANNEL_SECRET"]

line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(LINE_CHANNEL_SECRET)

@app.route("/raspi", methods=['POST'])
def raspi():
    raspi_id = request.json['raspi_id']
    content = request.json['content']
    target_users = User.query.filter_by(raspi_id=raspi_id).all()

    for user in target_users:
        line_bot_api.push_message(
            user.line_id,
            TextSendMessage(text=content)
        )

    return 'OK'

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@handler.add(MessageEvent)
def handle_message(event):
    event_type = event.source.type
    if event_type == 'user':
        sender_id = event.source.user_id

    elif event_type == 'group':
        sender_id = event.source.group_id

    elif event_type == 'room':
        sender_id = event.source.room_id

    sender = Status.query.filter_by(line_id=sender_id).one()

    print(sender_id)
    if sender.line_status == 0:
        if event.message.text == "登録":
            status = 1
            message = TextSendMessage(text="使用者の名前とラズパイIDを「、」区切りで入力してください\n(例)おばあちゃん、12345")

        elif event.message.text == "削除":
            status = 2
            message = TextSendMessage(text="削除したいラズパイIDを入力してください")

        elif event.message.text == "確認":
            raspis = User.query.filter_by(line_id=sender_id).all()
            text = "登録しているラズパイ一覧\n"
            for raspi in raspis:
                text += ("名前:" + raspi[0] + " ラズパイID:" + raspi[1] + "\n")
            message = TextSendMessage(text=text)

        else:
            status = 0
            message = TextSendMessage(text="通常メッセージ")

    elif (sender.line_status == 1):
        raspi = event.message.text.split('、')
        new_user = User(line_id=sender_id, user_name=raspi[0], raspi_id=raspi[1])
        db.session.add(new_user)
        db.session.commit()

        status = 0
        message = TextSendMessage(text="名前:" + raspi[0] + "\nラズパイID:" + raspi[1] + "\nで登録されました")

    else:
        return

    sender.line_status = status
    db.session.commit()

    line_bot_api.reply_message(
        event.reply_token,
        message
    )

@handler.add(FollowEvent)
def handle_follow(event):
    status = Status(line_id=event.source.user_id, line_status=0)
    db.session.add(status)
    db.session.commit()

    message = TextSendMessage(text="こんにちは")
    line_bot_api.reply_message(
        event.reply_token,
        message
    )

@handler.add(JoinEvent)
def handle_join(event):
    event_type = event.source.type
    if (event_type == 'group'):
        status = Status(line_id=event.source.group_id, line_status=0)

    elif (event_type == 'room'):
        status = Status(line_id=event.source.room_id, line_status=0)

    db.session.add(status)
    db.session.commit()

    message = TextSendMessage(text="こんにちは")
    line_bot_api.reply_message(
        event.reply_token,
        message
    )

if __name__ == "__main__":
    print("Please run run.py")
