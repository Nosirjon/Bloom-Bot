import telebot
from telebot import types
from aiogram.types.web_app_info import WebAppInfo


bot = telebot.TeleBot('6939780440:AAER7H3mcLR3e0oTlIW6OXc0ElmnlMiOpJ0') #token bot

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    markup.add(types.InlineKeyboardButton(text='Посетить сайт', web_app=types.WebAppInfo(url='https://gasoil.uz')))
    bot.send_message(message.chat.id, text='Здравствуйте я бот компании Bloom, бот пока же то на разработке вы можите посетить наш сайт нажав кнопку, посетить сайт.', reply_markup=markup)

bot.polling(non_stop=True)