from picture import photo_2
import telebot
from telebot import types,util
from other import analysis,sec_wea,ocr,search_title,voice_ocr
from telebot.types import InlineKeyboardMarkup,InlineKeyboardButton
from av import av
# from xiao import start_xiao,start_voice

TOKEN = '1150068914:AAGKIc1Pl7YLcAsb2aZDIxF4kYVCHoMB7Ks'

state_num = 0 #0为初始状态 1为查找 2为天气 3为查题
knownUsers = []
cate_dic={'自拍':0,'亚洲':1, '欧美':2 ,'美腿':3 , '清纯' : 4, '乱伦': 5, '卡通':6}

commands = {
    'start': '获取',
    'help': 'Gives you information about the available commands',
}
def gen_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 3
    markup.add(InlineKeyboardButton("再来一张"))
    return markup

imageSelect =  types.ReplyKeyboardMarkup(one_time_keyboard=True)  # 主菜单
imageSelect.add('图片', '小说','查题')
imageSelect.add('查找','一言','天气')
imageSelect_pic = types.ReplyKeyboardMarkup(one_time_keyboard=True)  # 图片下级菜单下级菜单
imageSelect_pic.add('返回','自拍', '亚洲')
imageSelect_pic.add('欧美','美腿', '清纯')
imageSelect_pic.add('乱伦','卡通','更多')
hideBoard = types.ReplyKeyboardRemove()  # if sent as reply_markup, will hide the keyboard


def listener(messages):         #日志
    for m in messages:
        if m.content_type == 'text':
            # print the sent message to the console
            print(str(m.chat.first_name) + " [" + str(m.chat.id) + "]: " + m.text)

def stanum(m,cid):
    global state_num
    if state_num == 1 and cid  in knownUsers:
        mags = av(m.text)
        lang = len(mags)
        if lang == 0:
            bot.send_message(cid, '请检查番号')
        else:
            for mag in mags:
                bot.send_message(cid, mag)
        state_num = 0
    elif state_num==2:
        data=sec_wea(m.text)
        bot.send_message(cid,data)
        state_num=0
    elif state_num==3:
        data = search_title(m.text)
        bot.send_message(cid,data)
    else:
        bot.send_message(cid,'请升级')
bot = telebot.TeleBot(TOKEN)
bot.set_update_listener(listener)  # 更新记录


@bot.message_handler(commands=['start'])
def command_start(m):
    cid = m.chat.id
    if cid not in knownUsers:
        bot.send_message(cid,'您是高级用户，可以使用全部功能')
        bot.send_message(cid,'start',reply_markup=imageSelect)
    else:
        bot.send_message(cid,'您的chat_id')
        bot.send_message(cid,cid)



@bot.message_handler(commands=['help'])
def command_help(m):
    cid = m.chat.id
    help_text = "The following commands are available: \n"
    for key in commands:  # generate help text out of the commands dictionary defined at the top
        help_text += "/" + key + ": "
        help_text += commands[key] + "\n"
    bot.send_message(cid, help_text)  # send the generated help page


@bot.message_handler(func=lambda message: True, content_types=['text'])
def command_default(m):
    cid = m.chat.id
    global state_num
    if m.text == '返回':
        bot.send_message(cid,'back',reply_markup=imageSelect)
        state_num = 0
        bot.send_message(cid,'已退出')
    elif state_num !=0:
        stanum(m,cid)
    elif m.text == '天气':
        state_num = 2
        bot.send_message(cid, '输入城市')
    # elif m.text == '小说' and cid in knownUsers:
    #     date = start_xiao()
    #     date = date.replace("\n", "")
    #     date = date.replace(" ", "")
    #     splitted_text = util.split_string(date, 3000)
    #     for text in splitted_text:
    #         bot.send_message(cid, text)
    # elif m.text=='有声' and cid in knownUsers:
    #     url = start_voice()
    #     if url:
    #         bot.send_voice(cid,url)
    elif m.text == '图片' and cid in knownUsers:
        bot.send_message(cid, "Please choose your image now", reply_markup=imageSelect_pic) #展开图片选择键盘
    elif m.text == '一言':
        bot.send_message(cid,analysis())
    elif m.text in cate_dic:
        bot.send_chat_action(cid, 'upload_photo')
        data = photo_2(cate_dic[m.text])
        if data :
            bot.send_photo(cid,data)       #发送图片并隐藏二级键盘
        else:bot.send_message(cid,'请重新获取')
    elif m.text == '查找' and cid in knownUsers:
        state_num = 1
        bot.send_message(cid,'输入番号')
    elif m.text == '查题':
        state_num = 3
        bot.send_message(cid,'已进入答题模式请发送返回退出')
    else:bot.send_message(cid,"Please try again")


@bot.message_handler(func=lambda message: True, content_types=['photo'])
def get_photo(m):
    cid = m.chat.id
    data = bot.get_file(m.photo[0].file_id)
    bot.send_message(cid,ocr(bot.download_file(data.file_path)))

@bot.message_handler(func=lambda message: True, content_types=['voice'])
def dati(m):
    # cid = m.chat.id
    # if state_num == 3:
    data = bot.get_file(m.voice.file_id)
    data = bot.download_file(data.file_path)
    text = voice_ocr(data)
    print(text)
    bot.send_message(m.chat.id,text)


bot.polling()
# while(1):
#     try:
#         bot.polling()
#     except:
#         bot.polling()

