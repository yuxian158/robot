from picture import get_url
from pyquery import PyQuery as pq
import random
from bs4 import BeautifulSoup
import re
from urllib import parse

# data = get_url('https://www.maomiav.com/assets/js/custom/config.js').text
# maomi = re.findall('www.*?.com', data)[2]
# r = get_url('https://'+maomi)
# print(r.text)
# reditList = r.history
# print(reditList)
# maomi=reditList[len(reditList)-1].headers["location"]
# maomi = re.search('www.(.*?).com',maomi).group(1)
maomi = 'abea553f0b134002.pw'

first_list_xiao=[
            'https://www.'+maomi+'.com/xiaoshuo/list-%E9%83%BD%E5%B8%82%E6%BF%80%E6%83%85',
            'https://www.'+maomi+'.com/xiaoshuo/list-%E4%BA%BA%E5%A6%BB%E4%BA%A4%E6%8D%A2',
            'https://www.'+maomi+'.com/xiaoshuo/list-%E6%A0%A1%E5%9B%AD%E6%98%A5%E8%89%B2',
            'https://www.'+maomi+'.com/xiaoshuo/list-%E5%AE%B6%E5%BA%AD%E4%B9%B1%E4%BC%A6',
            'https://www.'+maomi+'.com/xiaoshuo/list-%E6%83%85%E8%89%B2%E7%AC%91%E8%AF%9D',
            'https://www.'+maomi+'.com/xiaoshuo/list-%E6%80%A7%E7%88%B1%E6%8A%80%E5%B7%A7',
            'https://www.'+maomi+'.com/xiaoshuo/list-%E6%AD%A6%E4%BE%A0%E5%8F%A4%E5%85%B8',
            'https://www.'+maomi+'.com/xiaoshuo/list-%E5%8F%A6%E7%B1%BB%E5%B0%8F%E8%AF%B4',
             ]
first_list_voice = 'https://www.'+maomi+'.com/yousheng/list-%E8%AF%B1%E6%83%91%E7%9F%AD%E7%AF%87%E5%B0%8F%E8%AF%B4'
def xiao_second(url):#小说页解析
    data=get_url(url).text
    data = pq(data)
    data = data('.content').text()
    return data

def voice_secone(url):
    data=get_url(url).text
    print(data)
    data = pq(data)
    data = data('video')('source').attr('src')
    print(data)
    url = 'https://' + parse.quote(data[8:len(data)])
    return url

def xiao(url_first):        #小说列表页获取小说页
    data=get_url(url_first).text
    soup = BeautifulSoup(data,'lxml')
    uls=soup.find_all('ul')
    ulsq=uls[8]
    uls=ulsq.find_all('a')
    list={}
    for i in range(len(uls)-1):
        list[i]=uls[i].attrs['href']
    j = random.randint(0,17)
    url='https://www.'+maomi+'.com'+list[j]
    deta=xiao_second(url)
    return deta
def voice(url):
    data = get_url(url).text
    resulsts = re.findall('/yousheng/(\d{5}).html',data,re.S)
    if not resulsts:
        i = random.randint(0,len(resulsts)-1)
        url = 'https://www.hht979.com/yousheng/'+resulsts[i]+'.html'
        return voice_secone(url)
    else:
        return None
def generate(): #获取随机页码
    i=random.randint(0,7)
    j=random.randint(1,30)
    if j == 1:
        return first_list_xiao[i]+'.html'
    else:
        return first_list_xiao[i]+'-'+str(j)+'.html'
def gen_vioce():
    i = random.randint(0,30)
    if i == 0:
        return first_list_voice+'.html'
    else:
        return first_list_voice+'-'+str(i)+'.html'


def start_xiao():   #开始
    msg = xiao(generate())
    return msg

def start_voice():
    mag = voice(gen_vioce())
    return mag


print(start_xiao())

