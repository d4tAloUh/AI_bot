from .. import bot
from ..Parser import parse_sentence
from ..config import greetingTemplates
import random

@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    bot.send_message(message.chat.id, random.choice(greetingTemplates))


@bot.message_handler(func=lambda message: True)
def echo_message_handler(message):
    bot.send_message(message.chat.id, parse_sentence(message.text))
