import os
from unittest import result
from dotenv import load_dotenv
import telebot
import re

load_dotenv()
API_KEY = os.getenv('API_KEY')
bot = telebot.TeleBot(API_KEY)

whiteID = [1185083831,5175988241,1969603285,1317379638,761175875,1174929680,1518915241,1476158596,1195552086,1923316074,1299780896]


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


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "我是后台IP加白机器人,加白说明请输入/help查看")


@bot.message_handler(commands=['help'])
def help(message):
    introduce = '后台IP加白机器人说明：\n \
        1.加白IP命令：addip 项目名 IP地址，如：addip ww 1.1.1.1\n \
        2.删除IP命令：delip 项目名 IP地址，如：delip ww 1.1.1.1\n \
        3.项目名说明：\n\
            ng-南宫后台\n\
            c7-C7后台\n\
            28q-28圈后台\n\
            yh-壹号后台\n\
            wd-问鼎后台\n\
            ww-旺旺后台\n\
            hb-红包后台\n\
            c7team-C7推广后台\n\
            kf-客服后台\n\
            pp-匹配后台\n\
            hx-哈希后台'
    bot.reply_to(message, introduce)


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
        elif(item not in 'ng,c7,28q,yh,wd,ww,hb,c7team,kf,pp,hx'):
            bot.send_message(message.chat.id, '没有'+item+'这个项目')
        else:
            if(item == 'kf' and order == 'addip'):
                result = os.system(
                    'ansible-playbook /opt/chat_history/add_chat_history_admin_ip.yml -i /etc/ansible/hosts.kefu -e ip=%s' % ip)
                if(result == 0):
                    bot.send_message(message.chat.id, item+'添加ip:'+ip+'成功')
                else:
                    bot.send_message(message.chat.id, item+'添加ip:'+ip+'失败')
            elif(item == 'kf' and order == 'delip'):
                result = os.system(
                    'ansible-playbook /opt/chat_history/del_chat_history_admin_ip.yml -i /etc/ansible/hosts.kefu -e ip=%s' % ip)
                if(result == 0):
                    bot.send_message(message.chat.id, item+'删除ip:'+ip+'成功')
                else:
                    bot.send_message(message.chat.id, item+'删除ip:'+ip+'失败')
            elif(item == 'ww' and order == 'addip'):
                result = os.system(
                    'ansible-playbook /opt/wangwang/add_ww_admin_ip.yml -i /etc/ansible/hosts.wwadmin -e ip=%s' % ip)
                if(result == 0):
                    bot.send_message(message.chat.id, item+'添加ip:'+ip+'成功')
                else:
                    bot.send_message(message.chat.id, item+'添加ip:'+ip+'失败')
            elif(item == 'ww' and order == 'delip'):
                result = os.system(
                    'ansible-playbook /opt/wangwang/del_ww_admin_ip.yml -i /etc/ansible/hosts.wwadmin -e ip=%s' % ip)
                if(result == 0):
                    bot.send_message(message.chat.id, item+'删除ip:'+ip+'成功')
                else:
                    bot.send_message(message.chat.id, item+'删除ip:'+ip+'失败')
            elif(item == 'ng' and order == 'addip'):
                result = os.system(
                    'ansible-playbook /opt/whitened_bot/add_ng_admin_ip.yml -i /etc/ansible/hosts.whitened -e ip=%s' % ip)
                if(result == 0):
                    bot.send_message(message.chat.id, item+'添加ip:'+ip+'成功')
                else:
                    bot.send_message(message.chat.id, item+'添加ip:'+ip+'失败')
            elif(item == 'ng' and order == 'delip'):
                result = os.system(
                    'ansible-playbook /opt/whitened_bot/del_ng_admin_ip.yml -i /etc/ansible/hosts.whitened -e ip=%s' % ip)
                if(result == 0):
                    bot.send_message(message.chat.id, item+'删除ip:'+ip+'成功')
                else:
                    bot.send_message(message.chat.id, item+'删除ip:'+ip+'失败')
            elif(item in 'c7,c7team' and order == 'addip'):
                result = os.system(
                    'ansible-playbook /opt/whitened_bot/add_c7_admin_ip.yml -i /etc/ansible/hosts.whitened -e ip=%s' % ip)
                if(result == 0):
                    bot.send_message(message.chat.id, item+'添加ip:'+ip+'成功')
                else:
                    bot.send_message(message.chat.id, item+'添加ip:'+ip+'失败')
            elif(item in 'c7,c7team' and order == 'delip'):
                result = os.system(
                    'ansible-playbook /opt/whitened_bot/del_c7_admin_ip.yml -i /etc/ansible/hosts.whitened -e ip=%s' % ip)
                if(result == 0):
                    bot.send_message(message.chat.id, item+'删除ip:'+ip+'成功')
                else:
                    bot.send_message(message.chat.id, item+'删除ip:'+ip+'失败')
            elif(item == '28q' and order == 'addip'):
                result = os.system(
                    'ansible-playbook /opt/whitened_bot/add_28q_admin_ip.yml -i /etc/ansible/hosts.whitened -e ip=%s' % ip)
                if(result == 0):
                    bot.send_message(message.chat.id, item+'添加ip:'+ip+'成功')
                else:
                    bot.send_message(message.chat.id, item+'添加ip:'+ip+'失败')
            elif(item == '28q' and order == 'delip'):
                result = os.system(
                    'ansible-playbook /opt/whitened_bot/del_28q_admin_ip.yml -i /etc/ansible/hosts.whitened -e ip=%s' % ip)
                if(result == 0):
                    bot.send_message(message.chat.id, item+'删除ip:'+ip+'成功')
                else:
                    bot.send_message(message.chat.id, item+'删除ip:'+ip+'失败')
            elif(item == 'yh' and order == 'addip'):
                result = os.system(
                    'ansible-playbook /opt/whitened_bot/add_yh_admin_ip.yml -i /etc/ansible/hosts.whitened -e ip=%s' % ip)
                if(result == 0):
                    bot.send_message(message.chat.id, item+'添加ip:'+ip+'成功')
                else:
                    bot.send_message(message.chat.id, item+'添加ip:'+ip+'失败')
            elif(item == 'yh' and order == 'delip'):
                result = os.system(
                    'ansible-playbook /opt/whitened_bot/del_yh_admin_ip.yml -i /etc/ansible/hosts.whitened -e ip=%s' % ip)
                if(result == 0):
                    bot.send_message(message.chat.id, item+'删除ip:'+ip+'成功')
                else:
                    bot.send_message(message.chat.id, item+'删除ip:'+ip+'失败')
            elif(item == 'pp' and order == 'addip'):
                result = os.system(
                    'ansible-playbook /opt/whitened_bot/add_pp_admin_ip.yml -i /etc/ansible/hosts.whitened -e ip=%s' % ip)
                if(result == 0):
                    bot.send_message(message.chat.id, item+'添加ip:'+ip+'成功')
                else:
                    bot.send_message(message.chat.id, item+'添加ip:'+ip+'失败')
            elif(item == 'pp' and order == 'delip'):
                result = os.system(
                    'ansible-playbook /opt/whitened_bot/del_pp_admin_ip.yml -i /etc/ansible/hosts.whitened -e ip=%s' % ip)
                if(result == 0):
                    bot.send_message(message.chat.id, item+'删除ip:'+ip+'成功')
                else:
                    bot.send_message(message.chat.id, item+'删除ip:'+ip+'失败')
            elif(item == 'wd' and order == 'addip'):
                result = os.system(
                    'ansible-playbook /opt/whitened_bot/add_wd_admin_ip.yml -i /etc/ansible/hosts.whitened -e ip=%s' % ip)
                if(result == 0):
                    bot.send_message(message.chat.id, item+'添加ip:'+ip+'成功')
                else:
                    bot.send_message(message.chat.id, item+'添加ip:'+ip+'失败')
            elif(item == 'wd' and order == 'delip'):
                result = os.system(
                    'ansible-playbook /opt/whitened_bot/del_wd_admin_ip.yml -i /etc/ansible/hosts.whitened -e ip=%s' % ip)
                if(result == 0):
                    bot.send_message(message.chat.id, item+'删除ip:'+ip+'成功')
                else:
                    bot.send_message(message.chat.id, item+'删除ip:'+ip+'失败')
            elif(item == 'hb' and order == 'addip'):
                result = os.system(
                    'ansible-playbook /opt/whitened_bot/add_hb_admin_ip.yml -i /etc/ansible/hosts.whitened -e ip=%s' % ip)
                if(result == 0):
                    bot.send_message(message.chat.id, item+'添加ip:'+ip+'成功')
                else:
                    bot.send_message(message.chat.id, item+'添加ip:'+ip+'失败')
            elif(item == 'hb' and order == 'delip'):
                result = os.system(
                    'ansible-playbook /opt/whitened_bot/del_hb_admin_ip.yml -i /etc/ansible/hosts.whitened -e ip=%s' % ip)
                if(result == 0):
                    bot.send_message(message.chat.id, item+'删除ip:'+ip+'成功')
                else:
                    bot.send_message(message.chat.id, item+'删除ip:'+ip+'失败')
            elif(item == 'hx' and order == 'addip'):
                result = os.system(
                    'ansible-playbook /opt/whitened_bot/add_hx_admin_ip.yml -i /etc/ansible/hosts.whitened -e ip=%s' % ip)
                if(result == 0):
                    bot.send_message(message.chat.id, item+'添加ip:'+ip+'成功')
                else:
                    bot.send_message(message.chat.id, item+'添加ip:'+ip+'失败')
            elif(item == 'hx' and order == 'delip'):
                result = os.system(
                    'ansible-playbook /opt/whitened_bot/del_hx_admin_ip.yml -i /etc/ansible/hosts.whitened -e ip=%s' % ip)
                if(result == 0):
                    bot.send_message(message.chat.id, item+'删除ip:'+ip+'成功')
                else:
                    bot.send_message(message.chat.id, item+'删除ip:'+ip+'失败')
            else:
                bot.send_message(message.chat.id, '请输入加白或删除IP命令')


bot.polling()

