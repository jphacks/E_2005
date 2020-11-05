from flask import Flask, request, abort
from bot import app, db
from bot.models import User

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
            user.user_id,
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
    if (event_type == 'user'):
        sender_id = event.source.user_id

    elif (event_type == 'group'):
        sender_id = event.source.group_id

    elif (event_type == 'room'):
        sender_id = event.source.room_id

    print(sender_id)

    db_user = User.query.filter_by(user_id=sender_id).all()
    if (db_user == []):
        new_user = User(user_id=sender_id, raspi_id=event.message.text)
        db.session.add(new_user)
        db.session.commit()

        message = TextSendMessage(text="ラズパイIDを登録しました")
        print(User.query.all())

    else:
        user = User.query.filter(User.user_id==sender_id).one()
        print(user)
        message = TextSendMessage(text="ラズパイIDは"+user.raspi_id+"です。")

    if event.message.text == "bye":
        User.query.filter(User.user_id==sender_id).delete()
        db.session.commit()

        if event_type == 'group':
            line_bot_api.leave_group(sender_id)
            return
        elif event_type == 'room':
            line_bot_api.leave_room(sender_id)
            return
        elif event_type == 'user':
            message = TextSendMessage(text="ラズパイIDを削除しました。\n新しいラズパイIDを入力してください。")


    line_bot_api.reply_message(
        event.reply_token,
        message
    )

@handler.add(FollowEvent)
def handle_follow(event):
    message = TextSendMessage(text="ラズパイIDを入力してください")
    line_bot_api.reply_message(
        event.reply_token,
        message
    )

@handler.add(JoinEvent)
def handle_join(event):
    message = TextSendMessage(text="ラズパイIDを入力してください")
    line_bot_api.reply_message(
        event.reply_token,
        message
    )

if __name__ == "__main__":
    print("Please run run.py")
