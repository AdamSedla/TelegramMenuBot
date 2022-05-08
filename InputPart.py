import telebot
import Codes
import MenuPart
import datetime
import traceback
import sys
import os

from requests.exceptions import ConnectionError, ReadTimeout

bot = telebot.TeleBot(Codes.Token)
WeekendError = 42, 46

try:
    bot.send_message(
        Codes.ChatID,
        "Bot started"
    )
    while True:
        @bot.message_handler(commands=['start'])
        def help_command(message):
            try:
                bot.send_message(
                    message.chat.id,
                    "Hello there \n" +
                    "Pro více info /help"
                )
            except:
                print("Error in /start function")
        
        @bot.message_handler(commands=['help'])
        def help_command(message):
            try:
                bot.send_message(
                    message.chat.id,
                    "Menu pro dnešek: /menu \n" +
                    "Menu pro zvolený den: /daymenu"
                )
            except:
                print("Error in /help function")

        @bot.message_handler(commands=['menu'])
        def menu_command(message):
            try:
                day = datetime.datetime.today().weekday()
                               
                bot.send_chat_action(message.chat.id, 'typing')
                bot.send_message(
                    message.chat.id,
                    MenuPart.DayMenu(day)
                )

            except KeyError as WeekendError:
                bot.send_chat_action(message.chat.id, 'typing')
                bot.send_message(
                    message.chat.id,
                    "O víkendu zavřeno"
                )
               
            except:
               print("Error in /menu function")

        @bot.message_handler(commands=['daymenu'])
        def DayMenu_command(message):
            try:
                keyboard = telebot.types.InlineKeyboardMarkup()
                keyboard.row(
                    telebot.types.InlineKeyboardButton('Pondělí', callback_data='Monday'),
                    telebot.types.InlineKeyboardButton('Úterý', callback_data='Tuesday'),
                    telebot.types.InlineKeyboardButton('Středa', callback_data='Wednesday'),
                    telebot.types.InlineKeyboardButton('Čtvrtek', callback_data='Thursday'),
                    telebot.types.InlineKeyboardButton('Pátek', callback_data='Friday')
                )
                bot.send_chat_action(message.chat.id, 'typing')
                bot.send_message(
                    message.chat.id,
                    'Který den chcete vidět?',
                    reply_markup=keyboard
                )

                @bot.callback_query_handler(func=lambda call: True)
                def iq_callback(input):
                    data = input.data
                    def SendMenu(MessageDay):
                        bot.answer_callback_query(input.id)
                        bot.send_message(
                            message.chat.id,
                            MenuPart.DayMenu(MessageDay)
                        )

                    if data == 'Monday':
                        SendMenu(0)
                    elif data == 'Tuesday':
                        SendMenu(1)
                    elif data == 'Wednesday':
                        SendMenu(2)
                    elif data == 'Thursday':
                        SendMenu(3)
                    elif data == 'Friday':
                        SendMenu(4)
            except:
                print("Error in /daymenu function")

        bot.infinity_polling(timeout=10, long_polling_timeout = 5)
    bot.send_message(
        Codes.ChatID,
        "Bot Ended"
    )
        
except:
    traceback.print_exc()