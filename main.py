from fastapi import FastAPI
import telegram
import os


TOKEN = os.environ['TOKEN']
URL = os.environ['URL']

bot = telegram.Bot(token=TOKEN)
app = FastAPI()


@app.get("/")
async def root():
    # retrieve the message in JSON and then transform it to Telegram object
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
           Welcome to coolAvatar bot, the bot is using the service from http://avatars.adorable.io/ 
           to generate cool looking avatars based on the name you enter so please enter a name 
           and the bot will reply with an avatar for your name.
           """
        # send the welcoming message
        bot.sendMessage(chat_id=chat_id, text=bot_welcome, reply_to_message_id=msg_id)
    else:
        bot.sendMessage(chat_id=chat_id, photo=url, reply_to_message_id='Have a good day!')

    return 'ok'


@app.get('/setwebhook')
def set_webhook():
    # we use the bot object to link the bot to our app which live
    # in the link provided by URL
    s = bot.setWebhook(f'{URL}{TOKEN}')
    # something to let us know things work
    if s:
        return "webhook setup ok"
    else:
        return "webhook setup failed"
