import os
import telebot

bot = telebot.TeleBot(os.getenv("TOKEN"))
from bot.telegram import *
from bot.Parser import *


def run_parser():
    print("Parser is running")
    while True:
        text = input()
        print(parse_sentence(text))
        if text == 'c':
            break


def set_webhook():
    bot.set_webhook(url=f'{os.getenv("URL")}/bot{os.getenv("TOKEN")}')



def run_telegram_bot():
    bot.remove_webhook()
    print("Removed webhook")
    print("Bot started polling")
    bot.polling()
