import Codes
import MenuPart
import telebot

bot = telebot.TeleBot(Codes.Token)

try:
    bot.unpin_all_chat_messages(Codes.ChatID)
    Message = bot.send_message(
                Codes.ChatID,
                MenuPart.DayMenu(2)
                )
    MessageID = Message.message_id
    bot.pin_chat_message(Codes.ChatID, MessageID)
    
except:
    print("Error in DailyMenu.py")