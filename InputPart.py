import telebot
import Codes
import MenuPart

bot = telebot.TeleBot(Codes.Token)

@bot.message_handler(commands=['help'])
def help_command(message):
    bot.send_message(
        message.chat.id,
        "Hello there \n" +
        "Pro menu pro dnešek: /menu"
    )

@bot.message_handler(commands=['menu'])
def menu_command(message):
    bot.send_chat_action(message.chat.id, 'typing')
    bot.send_message(
        message.chat.id,
        MenuPart.Message
    )

@bot.message_handler(commands=['weekmenu'])
def WeekMenu_command(message):
    pass

    
@bot.message_handler(commands=['daymenu'])
def DayMenu_command(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton('Pondělí', callback_data='Monday'),
        telebot.types.InlineKeyboardButton('Úterý', callback_data='Tuesday'),
        telebot.types.InlineKeyboardButton('Středa', callback_data='Wednesday'),
        telebot.types.InlineKeyboardButton('Čtvrtek', callback_data='Thursday'),
        telebot.types.InlineKeyboardButton('Pátek', callback_data='Friday')
    )
    bot.send_message(
        message.chat.id,
        'Který den chcete vidět?',
        reply_markup=keyboard
    )
    @bot.callback_query_handler(func=lambda call: True)
    def iq_callback(input):
        data = input.data
        bot.send_message(
            message.chat.id,
            'Hello There'
        )


    



bot.polling(none_stop=True)