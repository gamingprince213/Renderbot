from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler
import os

TOKEN = os.environ.get("TELEGRAM_TOKEN")
bot = Bot(token=TOKEN)

app = Flask(__name__)

dispatcher = Dispatcher(bot, None, use_context=True)

def start(update, context):
    update.message.reply_text("Hello! Bot is working!")

dispatcher.add_handler(CommandHandler("start", start))

@app.route(f"/webhook/{TOKEN}", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return "ok"

@app.route("/", methods=["GET"])
def home():
    return "Bot is running!"

if __name__ == "__main__":
    app.run(port=10000)
