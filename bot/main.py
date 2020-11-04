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
    message = TextSendMessage(text=event.message.text)

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
