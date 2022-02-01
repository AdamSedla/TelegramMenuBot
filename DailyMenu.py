import requests
import Codes
import MenuPart
import datetime
import telebot






def telegram_bot_sendtext(bot_message):

    bot_token = Codes.Token
    bot_chatID = Codes.ChatID
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()




telegram_bot_sendtext(MenuPart.DayMenu(MenuPart.day))