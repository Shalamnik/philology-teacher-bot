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
        text = update.message.text.encode('utf-8').decode().lower()

        if text == "/start":
            reply_message = "Здравствуйте, я Ваш помощник по филологии: Русскому языку и литературе.\n" \
                            "Введите 'помощь' для просмотра возможных команд."
            bot.sendMessage(chat_id=chat_id, text=reply_message)
        elif text == "помощь":
            reply_message = "Для получения ДЗ введите свой класс, точку и слово 'дз'. Например, '5а.дз'.\n" \
                            "Для получения подсказки по ДЗ введите свой класс, точку и слово 'помощь'." \
                            "Например, '5а.помощь'.\n" \
                            "Для просмотра интересного факта о Русском языке введите 'интересное'."
            bot.sendMessage(chat_id=chat_id, text=reply_message)
        elif "5" in text and "дз" in text:
            reply_message = "Параграф 7, задание №3."
            bot.sendMessage(chat_id=chat_id, text=reply_message)
        elif "5" in text and "помощь" in text:
            reply_message = "Ещё раз внимательно прочитайте правило в параграфе и посмотрите контрольные примеры."
            bot.sendMessage(chat_id=chat_id, text=reply_message)
            photo_url = "https://www.google.com/imgres?imgurl=https%3A%2F%2Ffb.ru%2Fmisc%2Fi%2Fthumb%2Fa%2F4%2F6%2F1%2F2%2F7%2F2%2F461272.jpg&imgrefurl=https%3A%2F%2Ffb.ru%2Farticle%2F148730%2Fbezudarnaya-glasnaya-v-korne-proveryaemaya-udareniem-slova-bezudarnyie-glasnyie&tbnid=KoIQ_KYEZMr5sM&vet=12ahUKEwi4tZupl-70AhWPtIsKHbYLDwAQMygLegUIARDAAQ..i&docid=7C_dMZ0F4DdNLM&w=400&h=236&itg=1&q=%D0%B1%D0%B5%D0%B7%D1%83%D0%B4%D0%B0%D1%80%D0%BD%D0%B0%D1%8F%20%D0%B3%D0%BB%D0%B0%D1%81%D0%BD%D0%B0%D1%8F%20%D0%B2%20%D0%BA%D0%BE%D1%80%D0%BD%D0%B5&safe=active&ved=2ahUKEwi4tZupl-70AhWPtIsKHbYLDwAQMygLegUIARDAAQ"
            bot.sendPhoto(chat_id=chat_id, photo=photo_url)
        elif 'интерес' in text:
            photo_url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSDQCgyEPApE2KW-GpKjN5d1Ansehdxl5USvg&usqp=CAU'
            bot.sendPhoto(chat_id=chat_id, photo=photo_url)
        else:
            reply_message = "Команда не распознана. Попробуйте ввести ещё раз."
            bot.sendMessage(chat_id=chat_id, text=reply_message, reply_to_message_id=msg_id)
    # return request.json
    return {"ok": True}

