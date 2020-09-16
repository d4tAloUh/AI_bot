import os
import telebot
from pathlib import Path
from dotenv import load_dotenv

env_path = Path('.') / 'environment' / '.env'
load_dotenv(dotenv_path=env_path, verbose=True)
bot = telebot.TeleBot(os.getenv("TOKEN"))

from telegram_bot import *

if __name__ == '__main__':
    bot.polling()
