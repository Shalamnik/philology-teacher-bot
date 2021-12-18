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
        print(request.json)
        chat_id = request.json["message"]["chat"]["id"]
        send_message(chat_id, "pong")
    return request.json
