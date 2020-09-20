import os
import telebot

bot = telebot.TeleBot(os.getenv("TOKEN"))

from bot.telegram import *
from bot.Parser import *
from .config import greetingTemplates


def run_parser():
    print("TYPE c TO LEAVE")
    print(random.choice(greetingTemplates))

    while True:
        text = input()
        print(parse_sentence(text))
        if text == 'c':
            break


def run_telegram_bot():
    print("Bot started polling")
    bot.polling()
