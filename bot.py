import telebot
import datetime
import config
import sqlite3

TOKEN = (config.TOKEN)
bot = telebot.TeleBot(TOKEN)

sqlite3.connect('DATA.db')

@bot.message_handler(commands=['test'])
def canal(message):
    file = open('config.py', 'rb')
    bot.send_message('@adssdad', 'Hallo! Ich bin der Bot. Ein wünderschön Bot!')

@bot.message_handler(commands=['bild'])
def bild(message):
    photo = open('foto.jpeg', 'rb')
    bot.send_photo('@adssdad', photo)
    bot.send_message(message.chat.id, 'отправлено')



#file = open('config.py', 'w')

#@bot.message_handler(commands=['start'])
#def main(message):
   # msg = bot.send_message(message.chat.id, 'Введите ФИО')
    #bot.register_next_step_handler(msg, fio_step)

#def fio_step(message):
    #user_info = {}
    #user_info[''] = message.text
    #msg = bot.send_message(message.chat.id, 'Введите возраст')
   # bot.register_next_step_handler(msg, age_step, user_info)

#def age_step(message, user_info):
   # user_info[''] = message.text
   # print(user_info)

@bot.message_handler(content_types=['sticker'])
def sticker(message):
    bot.send_message(message.chat.id, "gut sticker")


bot.polling()

import telebot
import config

TOKEN = (config.TOKEN)
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,
                     'Приятно познакомиться! Я <b>Гена</b>. Я надеюсь вы дали мне админку в чате.\nПожалуйста, что бы продолжить работу со мной зарегистрируйтесь. Как? Напишите /reg. Удачи!',
                     parse_mode='HTML')


bot.polling()