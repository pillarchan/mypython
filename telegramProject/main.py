import os
from dotenv import load_dotenv
import telebot
import re
load_dotenv()
API_KEY = os.getenv('API_KEY')
bot = telebot.TeleBot(API_KEY)

whiteID = [761175875]


@bot.message_handler(commands=['hi', 'hello'])
def greet(message):
    bot.reply_to(message, "我是后台IP加白机器人")


def addip(message):
    request = message.text.split()
    if len(request) < 3 or request[0].lower() not in 'addip,delip':
        return False
    else:
        return True


def is_ip(ip):
    regexp = '^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
    if(re.match(regexp, ip)):
        return True
    else:
        return False


@bot.message_handler(func=addip)
def send_result(message):
    request = message.text.split()
    order, item, ip = request
    if(message.chat.id not in whiteID):
        bot.send_message(
            message.chat.id, 'ID未加白不能使用,请通知管理员加白ID:%s' % message.chat.id)
    else:
        if(is_ip(ip) == False):
            bot.send_message(message.chat.id, 'IP格式为1.1.1.1')
        elif(request[1] not in 'ng,c7,28q,yh,wd,ww,hb,c7team,kf'):
            bot.send_message(message.chat.id, '没有'+item+'这个项目')
        else:
            if(item == 'kf' and order == 'addip'):
                bot.send_message(message.chat.id, '哟西')


bot.polling()
