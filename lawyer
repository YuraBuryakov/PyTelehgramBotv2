import datetime
import json
import telebot
import requests
from bs4 import BeautifulSoup

#lawyer
bot = telebot.TeleBot('5676343264:AAHtpQ9N6w6zGsxWrjec8r19W7MuI8fW6mw')
#path = "venv/data_json.json"

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Hi! I am a Lawyer!")


@bot.message_handler(content_types="text")
def get_user_text(message):
    if message.text == 'Привет' or message.text == 'привет' or message.text == 'hi' or message.text == 'Hi':
        bot.send_message(message.chat.id, 'И тебе привет!')


bot.polling(none_stop=True)
