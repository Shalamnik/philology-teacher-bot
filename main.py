from flask import Flask, request
import telegram
import os


app = Flask(__name__)

TOKEN = os.environ['TOKEN']
URL = os.environ['URL']

bot = telegram.Bot(token=TOKEN)


@app.route('/', methods=['GET', 'POST'])
def receive_update():
    if request.method == "POST":
        print(request.json)
    return {"ok": True}
