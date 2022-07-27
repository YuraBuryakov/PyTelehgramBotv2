import telebot

bot = telebot.TeleBot('5376734562:AAExG2KHFDyrY4AedANB5YcaCV40cRORY0Q')
@bot.message_handler(commands=['start'])

def start(message):
    # mess = f'Hi, {message}' -- perfect command to study abilities of message
    mess = f'Hi, {message.from_user.first_name}'
    bot.send_message(message.chat.id, mess)

@bot.message_handler()
def get_user_text(message):
    if message.text == 'Привет' or  message.text == 'привет' or  message.text == 'hi' or  message.text == 'Hi':
        bot.send_message(message.chat.id, 'И тебе привет!')
    if message.text == "id" or message.text == "ID" or message.text == "Id":
        bot.send_message(message.chat.id, message.id)
bot.polling(none_stop=True)
