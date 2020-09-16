import os
import telebot

bot = telebot.TeleBot(os.getenv("TOKEN"))

from bot.telegram import *


def run_telegram_bot():
    bot.polling()
