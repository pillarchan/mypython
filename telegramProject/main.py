import os,telebot,re
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')
bot = telebot.TeleBot(API_KEY)

whiteID = os.getenv('WHITE_ID').split(',')
whiteIDInt = []
for i in whiteID:
    whiteIDInt.append(int(i))


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


hostsPath = '/etc/ansible/hosts.whitened'
items = [
    {'name': 'kf', 'addYmlPath': '/opt/whitened_bot/add_kf_admin_ip.yml',
        'delYmlPath': '/opt/whitened_bot/del_kf_admin_ip.yml'},
    {'name': 'ww', 'addYmlPath': '/opt/whitened_bot/add_ww_admin_ip.yml',
        'delYmlPath': '/opt/whitened_bot/del_ww_admin_ip.yml'},
    {'name': 'ng', 'addYmlPath': '/opt/whitened_bot/add_ng_admin_ip.yml',
        'delYmlPath': '/opt/whitened_bot/del_ng_admin_ip.yml'},
    {'name': 'c7', 'addYmlPath': '/opt/whitened_bot/add_c7_admin_ip.yml',
        'delYmlPath': '/opt/whitened_bot/del_c7_admin_ip.yml'},
    {'name': 'c7team', 'addYmlPath': '/opt/whitened_bot/add_c7team_admin_ip.yml',
        'delYmlPath': '/opt/whitened_bot/del_c7team_admin_ip.yml'},
    {'name': '28q', 'addYmlPath': '/opt/whitened_bot/add_28q_admin_ip.yml',
        'delYmlPath': '/opt/whitened_bot/del_28q_admin_ip.yml'},
    {'name': 'yh', 'addYmlPath': '/opt/whitened_bot/add_yh_admin_ip.yml',
        'delYmlPath': '/opt/whitened_bot/del_yh_admin_ip.yml'},
    {'name': 'pp', 'addYmlPath': '/opt/whitened_bot/add_pp_admin_ip.yml',
        'delYmlPath': '/opt/whitened_bot/del_pp_admin_ip.yml'},
    {'name': 'wd', 'addYmlPath': '/opt/whitened_bot/add_wd_admin_ip.yml',
        'delYmlPath': '/opt/whitened_bot/del_wd_admin_ip.yml'},
    {'name': 'hb', 'addYmlPath': '/opt/whitened_bot/add_hb_admin_ip.yml',
        'delYmlPath': '/opt/whitened_bot/del_hb_admin_ip.yml'},
    {'name': 'hx', 'addYmlPath': '/opt/whitened_bot/add_hx_admin_ip.yml',
        'delYmlPath': '/opt/whitened_bot/del_hx_admin_ip.yml'},
    {'name': 'newcard', 'addYmlPath': '/opt/whitened_bot/add_newcard_admin_ip.yml',
        'delYmlPath': '/opt/whitened_bot/del_newcard_admin_ip.yml'}
]
itemsList = 'ng,c7,28q,yh,wd,ww,hb,c7team,kf,pp,hx,newcard'

def chooseItem(item):
    for i in items:
        if(i['name'] == item):
            return i


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "????????????IP???????????????,?????????????????????/help??????")


@bot.message_handler(commands=['help'])
def help(message):
    introduce = '??????IP????????????????????????\n \
        1.??????IP?????????addip ????????? IP???????????????addip ww 1.1.1.1\n \
        2.??????IP?????????delip ????????? IP???????????????delip ww 1.1.1.1\n \
        3.??????????????????\n\
            ng-????????????\n\
            c7-C7??????\n\
            28q-28?????????\n\
            yh-????????????\n\
            wd-????????????\n\
            ww-????????????\n\
            hb-????????????\n\
            c7team-C7????????????\n\
            kf-????????????\n\
            pp-????????????\n\
            hx-????????????\n\
            newcard-?????????????????????'
    bot.reply_to(message, introduce)


@bot.message_handler(func=addip)
def send_res(message):
    request = message.text.split()
    order, item, ip = request
    if(message.chat.id not in whiteIDInt):
        bot.send_message(
            message.chat.id, 'ID?????????????????????,????????????????????????ID:%s' % message.chat.id)
    else:
        if(is_ip(ip) == False):
            bot.send_message(message.chat.id, 'IP?????????1.1.1.1')
        elif(item not in itemsList):
            bot.send_message(message.chat.id, '??????'+item+'????????????')
        else:
            myitem = chooseItem(item)
            if(order == 'addip'):
                res = os.system(
                    'ansible-playbook ' + myitem['addYmlPath'] + ' -i ' + hostsPath + ' -e ip=%s' % ip)
                if(res == 0):
                    bot.send_message(message.chat.id, item+'??????ip:'+ip+'??????')
                else:
                    bot.send_message(message.chat.id, item+'??????ip:'+ip+'??????')
            elif(order == 'delip'):
                res = os.system(
                    'ansible-playbook ' + myitem['delYmlPath'] + ' -i ' + hostsPath + ' -e ip=%s' % ip)
                if(res == 0):
                    bot.send_message(message.chat.id, item+'??????ip:'+ip+'??????')
                else:
                    bot.send_message(message.chat.id, item+'??????ip:'+ip+'??????')
            else:
                bot.send_message(message.chat.id, '????????????????????????IP??????')


bot.polling()

