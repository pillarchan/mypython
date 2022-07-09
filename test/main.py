import os
import re
import telebot
import sys

myfr = open('test\.env', 'r')

arrFile = myfr.readlines().copy()
fileContent = ''.join(arrFile)
API_KEY_CUT = arrFile[0][arrFile[0].index('\'')+1:-2]
WHITE_ID_CUT = arrFile[1][arrFile[1].index('\'')+1:-1]

WHITE_ID_ARRAY = WHITE_ID_CUT.split(',')
WHITE_ID_INT = []
for i in WHITE_ID_ARRAY:
    WHITE_ID_INT.append(int(i))

myfw = open('test\.env', 'w')
myfw.write(fileContent)
myfw.close()
myfr.close()

print(API_KEY_CUT,WHITE_ID_INT)


bot = telebot.TeleBot(API_KEY_CUT)


@bot.message_handler()
def send_result(message):
    bot.send_message(message.chat.id,str(WHITE_ID_INT))


bot.polling()
