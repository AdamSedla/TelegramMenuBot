# TelegramMenuBot
 Bot adding Scholarest menu everyday into Telegram group

## How does it work:
After Telegram command from user, program uses Pandas library to take data from google sheets menu. This data is then taken and sent to user via Telegram.

## Installation  
1.) Install all python libraries written in requirments.txt
2.) Use BotFather on Telegram to make your own bot  
2.1.) Setup your bot  
3.) Create Codes.py  
4.) Write your token from BotFather to column YOUR_TOKEN  
4.1.)   
Token = "YOUR_TOKEN"  
GSheet = "1JpEUpUJ3slFP1y2PgJV1J_2_sBf5VOek4TUcq90P_Cs"  
5.) Put part 3.1. above inside Codes.py  
6.) Start InputPart.py  

## Commands:  
/start - starter command  
/help - sends you all available commands  
/menu - sends you menu for today  
/daymenu - lets you choose for which day you wanna see menu  

## Known issues:  
bot might sometimes crash on server, due to unknown reasons  