import telebot
import config
import random
from telebot import types



bot = telebot.TeleBot(config.TOKEN)
# keyboard
@bot.message_handler(commands=['start'])
def lala(message):
    k = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Random number")
    item2 = types.KeyboardButton("How r u?")

    k.add(item1, item2)
    bot.send_message(message.chat.id, "Добро пожаловать\n на мой первый телеграм бот", reply_markup=k)


# inline keyboard


@bot.message_handler(content_types=['text'])
def sms(message):
    if message.chat.type == 'private':
        if message.text == 'Random number':
            bot.send_message(message.chat.id, str(random.randint(0, 100)))
        elif message.text == "How r u?":
            k = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("good", callback_data='good')
            item2 = types.InlineKeyboardButton("bad", callback_data="bad")

            k.add(item1, item2)
            bot.send_message(message.chat.id, 'Fine, what about u?', reply_markup=k)

        else:
            bot.send_message(message.chat.id, 'What?')


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'good':
                bot.send_message(call.message.chat.id, 'Well')
            elif call.data == 'bad':
                bot.send_message(call.message.chat.id, "It's not my problem")

    except Exception as e:
        print(repr(e))

bot.polling(none_stop=True)
