from flask import Flask, request
import telegram
import os
import requests


app = Flask(__name__)

TOKEN = os.environ['TOKEN']
URL = os.environ['URL']

bot = telegram.Bot(token=TOKEN)


def send_message(chat_id, text):
    method = "sendMessage"
    url = f"https://api.telegram.org/bot{TOKEN}/{method}"
    data = {"chat_id": chat_id, "text": text}
    requests.post(url, data=data)


@app.route("/", methods=["GET", "POST"])
def receive_update():
    if request.method == "POST":
        update = telegram.Update.de_json(request.get_json(force=True), bot)

        chat_id = update.message.chat.id
        msg_id = update.message.message_id

        # Telegram understands UTF-8, so encode text for unicode compatibility
        text = update.message.text.encode('utf-8').decode()
        # for debugging purposes only
        print("got text message :", text)
        # the first time you chat with the bot AKA the welcoming message
        if text == "/start":
            # print the welcoming message
            bot_welcome = """
               Welcome to coolAvatar bot, the bot is using the service from http://avatars.adorable.io/ to generate cool looking avatars based on the name you enter so please enter a name and the bot will reply with an avatar for your name.
               """
            # send the welcoming message
            bot.sendMessage(chat_id=chat_id, text=bot_welcome, reply_to_message_id=msg_id)
    # return request.json
    return {"ok": True}

