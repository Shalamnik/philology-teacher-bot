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
        text = update.message.text.encode('utf-8').decode()

        if text == "/start":
            reply_message = "Здравствуйте, я Ваш помощник по филологии: Русскому языку и литературе.\n" \
                            "Введите 'помощь' для просмотра возможных команд."
            bot.sendMessage(chat_id=chat_id, text=reply_message)
        elif text == "помощь":
            reply_message = "Для получения ДЗ введите свой класс, точку и слово 'дз'. Например, '5а.дз'.\n" \
                            "Для получения подсказки по ДЗ введите свой класс, точку и слово 'помощь'. " \
                            "Например, '5а.помощь'."
            bot.sendMessage(chat_id=chat_id, text=reply_message)
        elif "5" in text and "дз" in text:
            reply_message = "Параграф 7, задание №3."
            bot.sendMessage(chat_id=chat_id, text=reply_message)
        elif "5" in text and "помощь" in text:
            reply_message = "Ещё раз внимательно прочитайте правило в параграфе и посмотрите контрольные примеры."
            bot.sendMessage(chat_id=chat_id, text=reply_message)
        else:
            reply_message = "Команда не распознана. Попробуйте ввести ещё раз."
            bot.sendMessage(chat_id=chat_id, text=reply_message, reply_to_message_id=msg_id)
    # return request.json
    return {"ok": True}

