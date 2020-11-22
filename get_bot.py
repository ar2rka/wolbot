import os
import telebot


def get_bot():
    ttoken = os.getenv('TTOKEN')
    bot = telebot.TeleBot(ttoken, parse_mode=None)
    return bot