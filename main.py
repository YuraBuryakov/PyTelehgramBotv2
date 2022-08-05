import datetime
import json
import telebot

bot = telebot.TeleBot('5376734562:AAExG2KHFDyrY4AedANB5YcaCV40cRORY0Q')
path = "venv/data_json.json"

@bot.message_handler(commands=['start'])
def start(message):
    # mess = f'Hi, {message}' -- perfect command to study abilities of message
    mess = f'Hi, {message.from_user.first_name}! Чтобы общаться со мной - напишите лично мне в чате или создайтк личную переписку со мной.'
    bot.send_message(message.chat.id, mess)
    #add a new telegram user into json file
    def write_json(data, filename = path):
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
    # opens json file end checks a telegram user (does he exist in json file or not)
        temp = Open_Json_File_Read()
        count = 0
        for item in temp:
            if item["chat_id"] == message.chat.id:
                count = count + 1
        if count == 0:
             y = {"firstname": message.from_user.first_name, "chat_id": message.chat.id,"note": "empty" ,"score": 0}
             temp.append(y)
             write_json(data)

    bot.send_message(message.chat.id, List_Of_Commands())


@bot.message_handler()
def get_user_text(message):
    if message.text == 'Привет' or message.text == 'привет' or message.text == 'hi' or message.text == 'Hi':
        bot.send_message(message.chat.id, 'И тебе привет!')
    if message.text == "id" or message.text == "ID" or message.text == "Id":
        bot.send_message(message.chat.id, message.id)
    if message.text == "дата" or message.text == "Дата" or message.text == "date" or message.text == "Date":
        bot.send_message(message.chat.id, datetime.date.today())
    if message.text == "Работаешь" or message.text == "работаешь" or message.text == "Работаешь ?" or message.text == "работаешь ?":
        bot.send_message(message.chat.id, "Да! Уже в Работе!")
    if message.text == "Счет" or message.text == "счет" or  message.text == "Счёт" or message.text == "счёт":
        Score(message)
    if message.text == "Login" or message.text == "login" or message.text == "Логин" or message.text == "логин":
        bot.send_message(message.chat.id, "Please enter a password/ Пожалуйста, введите пароль")
        if message.text == "cicerone":
            bot.send_message(message.chat.id, "Hi, Admin")


# send a telegram users' score
def Score(message):
    score = Get_Data_From_Json("score",message.chat.id)
    bot.send_message(message.chat.id, "У тебя " + str(score) + " социальных очков")

#gets the json value
def Get_Data_From_Json(key, message_id):
    if message_id > 0:
            temp = Open_Json_File_Read()
            for item in temp:
                if item["chat_id"] == message_id:
                    return item[key]
    else:
        return -9

#open json file for reading and get a list
def Open_Json_File_Read():
    with open(path, 'r') as j:
        data = json.loads(j.read())
        temp = data["telegram_user"]
        return temp

#list of commands which a bot can do
def List_Of_Commands():
    mess = "Команды \n" \
            "На данный момент я способен отзываться на такие команды:\n" \
            " - /start\n" \
           " - Работаешь\n" \
           " - Счет\n" \
           ""
    return mess

# funciton which use a word "stop" to stop every command in a chat

bot.polling(none_stop=True)

