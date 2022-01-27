import requests
import Codes
import GSheetPart
import time
import datetime

Message = "Menu pro dnešek:" + "\n\n"

def telegram_bot_sendtext(bot_message):

    bot_token = Codes.Token
    bot_chatID = Codes.ChatID
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()

try:
    for key, value in GSheetPart.Menu.items():
        Message += key + "\n" + value + "\n\n"
except:
    Message = "Error 666" + "\n" + "Dnes bude karbanátek po Ukrajinsku podle strýčka Stalina"

telegram_bot_sendtext(Message)