import os
import telebot
import random

bot = telebot.TeleBot(os.getenv("TOKEN"))

from bot.telegram import *
from bot.Parser import *
from .config import greetingTemplates


def run_parser():
    print(random.choice(greetingTemplates))
    while True:
        text = input()
        print(parse_sentence(text))
        if text == 'c':
            break


def set_webhook():
    bot.set_webhook(url=f'{os.getenv("URL")}/bot{os.getenv("TOKEN")}')
    print("webhook setted up")


def run_telegram_bot():
    bot.remove_webhook()
    print("Removed webhook")
    print("Bot started polling")
    bot.polling()
