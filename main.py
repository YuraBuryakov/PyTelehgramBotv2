import datetime
import json

import telebot

bot = telebot.TeleBot('5376734562:AAExG2KHFDyrY4AedANB5YcaCV40cRORY0Q')
@bot.message_handler(commands=['start'])
def start(message):
    # mess = f'Hi, {message}' -- perfect command to study abilities of message
    mess = f'Hi, {message.from_user.first_name}'
    bot.send_message(message.chat.id, mess)

@bot.message_handler()
def get_user_text(message):
    if message.text == 'Привет' or message.text == 'привет' or message.text == 'hi' or message.text == 'Hi':
        bot.send_message(message.chat.id, 'И тебе привет!')
    if message.text == "id" or message.text == "ID" or message.text == "Id":
        bot.send_message(message.chat.id, message.id )
    if message.text == "время" or message.text == "Время":
        bot.send_message(message.chat.id, datetime.date.today() )
    if message.text == "Работаешь" or message.text == "работаешь" or message.text == "Работаешь ?" or message.text == "работаешь ?":
        bot.send_message(message.chat.id, "Да! Уже в Работе!")
    if message.text == "Счет" or message.text == "счет":
        Score(message)


@bot.message_handler(commands=['score'])
def get_score (message):
    bot.send_message(message.chat.id, "Your score is")

def Score(message):

    #bot.send_message(message.chat.id, Open_Data_File_())
    score =  Open_Data_Json_File()
    bot.send_message(message.chat.id, "У тебя " + score + "социальных очков")
def Open_Data_File_():
    #f = open("data.txt","a")
   # f.write("Now the file has more content")
   # f.close()

    f = open("data.txt", "r")
    val = f.read()
    f.close()
    return (val)
def Open_Data_Json_File():
    
    path = "PyTelehgramBotv2/data_json.json"
    with open(path, 'r') as j:
        data = json.loads(j.read())
        return str(data['score'])

bot.polling(none_stop=True)

