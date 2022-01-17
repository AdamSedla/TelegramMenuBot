import requests
import Codes
import GSheetPart

def telegram_bot_sendtext(bot_message):
    

    bot_token = Codes.Token
    bot_chatID = Codes.ChatID
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()



for key, value in GSheetPart.ChooseDay().items():
    telegram_bot_sendtext(value)



#for key, value in GSheetPart.Monday.items() :
#    print (telegram_bot_sendtext(value))

