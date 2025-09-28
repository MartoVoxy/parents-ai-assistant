import os
from telegram import Bot
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
bot = Bot(token=TELEGRAM_TOKEN)

def send_telegram_message(chat_id, text):
    bot.send_message(chat_id=chat_id, text=text, parse_mode='Markdown')
