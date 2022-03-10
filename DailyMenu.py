import Codes
import MenuPart
import telebot
import datetime

bot = telebot.TeleBot(Codes.Token)

day = datetime.datetime.today().weekday()


try:
    bot.unpin_all_chat_messages(Codes.ChatID_CoolKids)
    Message = bot.send_message(
                Codes.ChatID_CoolKids,
                MenuPart.DayMenu(day)
                )
    MessageID = Message.message_id
    bot.pin_chat_message(Codes.ChatID_CoolKids, MessageID, True)
except:
    print("Error in DailyMenu.py")