import os
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('LINE_CHANNEL_ACCESS_TOKEN')
handler = WebhookHandler('LINE_CHANNEL_SECRET')


@app.route("/callback", methods=['POST'])
def callback():
    # Get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # Get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # Handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage) # hanya teks
def handle_message(event): # handling event 
    """ Here's all the messages will be handled and processed by the program """
    
    msg = (event.message.text).lower()

    if 'hello' in msg:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="Halo juga!"))
    elif 'apa kabar' in msg:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="Baik!"))
    elif 'siapa anda' in msg:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="Saya bot!"))
    else: 
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=event.message.text)) 

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)