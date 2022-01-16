import requests
import Codes

def telegram_bot_sendtext(bot_message):
    
    bot_message = "Hi"

    bot_token = Codes.Token
    bot_chatID = Codes.ChatID
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()

    
print(telegram_bot_sendtext("HelloThr"))