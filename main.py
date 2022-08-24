
import datetime
import json
import telebot

import requests
from bs4 import BeautifulSoup
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor


bot = telebot.TeleBot('5376734562:AAExG2KHFDyrY4AedANB5YcaCV40cRORY0Q')
path = "data_json.json"


@bot.message_handler(commands=['start'])
def start(message):
    keyboard_start = InlineKeyboardMarkup()
    washing_machine_button = InlineKeyboardButton(text="Pracka", callback_data="washing_machine_callback")
    do_you_work_button = InlineKeyboardButton(text="Are you working?", callback_data="do_you_work_button_callback")
    keyboard_start.add(washing_machine_button)
    keyboard_start.add(do_you_work_button)




    # takes info from a new user
    info = f'firstname: {message.from_user.first_name} \n' \
           f'chat_id: {message.chat.id} \n' \
           f'note: 0 \n' \
           f'score: 0 \n'
    # mess = f'Hi, {message}' -- perfect command to study abilities of message
    # mess = f'Hi, {message.from_user.first_name}! Чтобы общаться со мной - напишите лично мне в чате или создайте личную переписку со мной.'
    # sends to my chat an info
    bot.send_message(message.chat.id, "Привет! Чем могу помочь?",reply_markup=keyboard_start)
    bot.send_message(914254077, info)
    # bot.send_message(message.chat.id, mess)

    # add a new telegram user into json file
    def write_json(data, filename=path):
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
        # opens json file end checks a telegram user (does he exist in json file or not)
        temp = Open_Json_File_Read()
        count = 0
        for item in temp:
            if item["chat_id"] == message.chat.id:
                count = count + 1
        if count == 0:
            y = {"firstname": message.from_user.first_name, "chat_id": message.chat.id, "note": "empty", "score": 0}
            temp.append(y)
            write_json(data)

    # bot.send_message(message.chat.id, List_Of_Commands())


# @bot.message_handler()
# def get_user_text(message):
#     keyboard = InlineKeyboardMarkup()
#     washing_machine_button = InlineKeyboardButton(text="Pracka", callback_data="washing_machine_callback")
#     do_you_work_button = InlineKeyboardButton(text="Are you working?", callback_data="do_you_work_button_callback")
#     keyboard.add(washing_machine_button)
#     keyboard.add(do_you_work_button)
#
#     if message.text == 'Привет' or message.text == 'привет' or message.text == 'hi' or message.text == 'Hi':
#         bot.send_message(message.chat.id, 'И тебе привет!')
#     if message.text == "Прачка" or message.text == "прачка":
#         bot.send_message(message.chat.id, Washing_Machine_Status())
#     if message.text == "Работаешь" or message.text == "работаешь" or message.text == "Работаешь ?" or message.text == "работаешь ?":
#         bot.send_message(message.chat.id, "Да! Уже в Работе!")



# send a telegram users' score
def Score(message):
    score = Get_Data_From_Json("score", message.chat.id)
    bot.send_message(message.chat.id, "У тебя " + str(score) + " социальных очков")


# gets the json value
def Get_Data_From_Json(key, message_id):
    if message_id > 0:
        temp = Open_Json_File_Read()
        for item in temp:
            if item["chat_id"] == message_id:
                return item[key]
    else:
        return -9


# open json file for reading and get a list
def Open_Json_File_Read():
    with open(path, 'r') as j:
        data = json.loads(j.read())
        temp = data["telegram_user"]
        return temp


# list of commands which a bot can do
def List_Of_Commands():
    mess = "Команды \n" \
           "На данный момент я способен отзываться на такие команды:\n" \
           " - /start\n" \
           " - Прачка / прачка \n" \
           " - Работаешь\n" \
           " - Счет\n" \
           " - Плюс очко \n "

    return mess

@bot.callback_query_handler(func=lambda c:True)
def send_random_value(call: types.CallbackQuery):
    # if call.data == 'random_value':
    #     bot.send_message(call.message.chat.id, str(randint(1,10)))
    #     call.answer()
    if call.data == 'washing_machine_callback':
        bot.send_message(call.message.chat.id, Washing_Machine_Status())
        call.answer()
    if call.data == 'do_you_work_button_callback':
        bot.send_message(call.message.chat.id, "Да! Уже в Работе!")
        call.answer()

# Replace data in json
def Replace_In_Json(key, message):
    temp = Open_Json_File_Read()
    count = 0
    for item in temp:
        if item["chat_id"] == message.chat.id:
            temp[count][key] += 1
            write_json(temp)
        else:
            count += 1


# Change tne value or add new in json
def write_json(data, filename=path):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)


# *******washing machine********
def Washing_Machine_Status():
    url_washing_machine = "https://hk.cvut.cz/en/about-us/"
    req = requests.get(url=url_washing_machine)
    src = req.text
    soup = BeautifulSoup(src, "lxml")
    machines = soup.find("aside", class_="widget widget_xyz_insert_php_widget").findAll("li")
    mess = ""
    for item in machines:
        mess = mess + item.text + "\n"
    return mess


bot.polling(none_stop=True)
