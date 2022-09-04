

import telebot
from telebot import types

token='5343558513:AAFYXAF628RYEz6PInybmD1SG2mDl85R7Yg'
bot = telebot.TeleBot(token)


def create_keyboard():
    keyboard = types.InlineKeyboardMarkup()
    drink_btn = types.InlineKeyboardButton(text="Хочу пить", callback_data='1')
    eat_btn = types.InlineKeyboardButton(text="Хочу есть", callback_data='2')
    wolk_btn = types.InlineKeyboardButton(text="Хочу гулять", callback_data='3')
    slip_btn = types.InlineKeyboardButton(text="Хочу спать", callback_data='4')
    joke_btn = types.InlineKeyboardButton(text="Хочу шутку", callback_data='5')
    keyboard.add(drink_btn)
    keyboard.add(eat_btn)
    keyboard.add(wolk_btn)
    keyboard.add(slip_btn)
    keyboard.add(joke_btn)
    return keyboard

@bot.message_handler(commands=['start'])
def start_bot(message):
    keyboard=create_keyboard()
    bot.send_message(
        message.chat.id,
        "Добрый день! Выберите, что Вы хотите",
        reply_markup=keyboard
    )

@bot.callback_query_handler(func=lambda call:True)
def callback_inline(call):
    keyboard = create_keyboard()
    if call.message:
        if call.data=="1":
            img = open('вода.jpg','rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption="Утолять жажду - одно из самых острых наслаждений",
                reply_markup=keyboard)
            img.close()
        if call.data == "2":
            img = open('еда.jpg', 'rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption="Голод - лучшая приправа к пище",
                reply_markup=keyboard)
            img.close()
        if call.data == "3":
            img = open('гулять.jpg', 'rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption="Не придумывай себе занятий, всю работу не переделаешь"
                        "Иди и гуляй тогда и работа станет не в тягость",
                reply_markup=keyboard)
            img.close()
        if call.data == "4":
            img = open('спать.jpg', 'rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption="Кто хочет много знать"
                        "Тому надо мало спать",
                reply_markup=keyboard)
            img.close()
        if call.data == "5":
            img = open('шутка.jpg', 'rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption="Правда жизни :)",
                reply_markup=keyboard)
            img.close()


if __name__=="__main__":
    bot.polling(none_stop=True)