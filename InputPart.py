import telebot
import Codes
import TelegramPart

bot = telebot.TeleBot(Codes.Token)

@bot.message_handler(commands=['help'])
def help_command(message):
    bot.send_message(
        message.chat.id,
        "Hello there \n" +
        "Pro menu pro dnešek /menu"
    )

@bot.message_handler(commands=['menu'])
def menu_command(message):
    bot.send_message(
        message.chat.id,
        TelegramPart.Message
    )

bot.polling(none_stop=True)