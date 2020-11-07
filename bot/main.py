from flask import Flask, request, abort, render_templatei, redirect, url_for
from bot import app, db
from bot.models import User, Status, Whole, Call
from bot.wakati import wakati

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
import random, string

#環境変数取得
LINE_CHANNEL_ACCESS_TOKEN = os.environ["LINE_CHANNEL_ACCESS_TOKEN"]
LINE_CHANNEL_SECRET = os.environ["LINE_CHANNEL_SECRET"]

line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(LINE_CHANNEL_SECRET)

def convert_skull_from_num(num):
    msg = ""
    num = 3 if num > 3 else num
    for i in range(num):
        msg += "☠"
    return msg.ljust(3, "●")

def get_words_dict_from_db(tags):
    tag_words = {"money": [], "job": [], "situation": [], "promise": [], "person": []}
    for tag in tags:
        whole_words = Whole.query.filter_by(tag = tag).all()
        for word in whole_words:
            tag_words[tag].append(word.word)

    return tag_words

def randomname(n):
   return ''.join(random.choices(string.ascii_letters + string.digits, k=n))

@app.route("/raspi", methods=['POST'])
def raspi():
    raspi_id = request.json['raspi_id']
    text = request.json['content']
    target_users = User.query.filter_by(raspi_id=raspi_id).all()
    tags = ["money", "job", "situation", "promise", "person"]
    tag_counts = {"money": 0, "job": 0, "situation": 0, "promise": 0, "person": 0}
    pass_key = randomname(10)

    tag_words = get_words_dict_from_db(tags)
    words = wakati(text)

    for tag in tags:
        for word in tag_words[tag]:
            if word in words:
                tag_counts[tag] += 1

    score_content = user.user_name + "さんに電話がかかってきました\n以下のような危険性があります\n"
    for tag, count in tag_counts.items():
        score_content += tag + "\n" + convert_skull_from_num(count) + "\n\n"

    new_call = Call(raspi_id=raspi_id, text=text, key=pass_key)
    db.session.add(new_call)
    db.session.commit()

    fb_content = "https://fraud-checker-test.herokuapp.com/feedback/" + pass_key

    for user in target_users:
        line_bot_api.push_message(
            user.line_id,
            TextSendMessage(text=score_content)
        )

        line_bot_api.push_message(
            user.line_id,
            TextSendMessage(text=fb_content)
        )

    return 'OK'

@app.route('/feedback/<key>', methods=['GET', 'POST'])
def feedback(key):
    if request.method == 'GET':
        return render_template(feedback.html)

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
            raspis = User.query.filter_by(line_id=sender_id).all()

            if raspis == []:
                text = "登録しているラズパイはありません"
                status = 0
            else:
                text = "削除したいラズパイIDを入力してください\n登録しているラズパイ一覧"
                for raspi in raspis:
                    text += ("\n名前:" + raspi.user_name + " ラズパイID:" + raspi.raspi_id)
                status = 2

            message = TextSendMessage(text=text)

        elif event.message.text == "確認":
            raspis = User.query.filter_by(line_id=sender_id).all()

            if raspis == []:
                text = "登録しているラズパイはありません"
            else:
                text = "登録しているラズパイ一覧"
                for raspi in raspis:
                    text += ("\n名前:" + raspi.user_name + " ラズパイID:" + raspi.raspi_id)

            status = 0
            message = TextSendMessage(text=text)

        elif event.message.text == "バイバイ":
            if event_type == 'group':
                User.query.filter(User.line_id==sender_id).delete()
                db.session.commit()
                line_bot_api.leave_group(sender_id)
                return
            elif event_type == 'room':
                User.query.filter(User.line_id==sender_id).delete()
                db.session.commit()
                line_bot_api.leave_room(sender_id)
                return

        else:
            status = 0
            text = "ラズパイIDを登録したいときは「登録」\n確認したいときは「確認」\n削除したいときは「削除」"
            if event_type == 'group' or event_type == 'room':
                text += "\n退会させたい時は「バイバイ」"
            text += "\nと入力してください"

            message = TextSendMessage(text=text)

    elif sender.line_status == 1:
        raspi = event.message.text.split('、')

        if len(raspi) == 2:
            new_user = User(line_id=sender_id, user_name=raspi[0], raspi_id=raspi[1])
            db.session.add(new_user)
            db.session.commit()

            message = TextSendMessage(text="名前:" + raspi[0] + "\nラズパイID:" + raspi[1] + "\nで登録されました")
        else:
            message = TextSendMessage(text="指定した形で入力してください")
        
        status = 0

    elif sender.line_status == 2:
        raspis = User.query.filter_by(line_id=sender_id).all()
        text = event.message.text + "は登録されていません"

        for raspi in raspis:
            if raspi.raspi_id == event.message.text:
                User.query.filter(User.raspi_id==event.message.text).delete()
                db.session.commit()
                text = event.message.text + "を削除しました"

        status = 0
        message = TextSendMessage(text=text)

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
