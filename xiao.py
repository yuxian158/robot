from picture import get_url
from pyquery import PyQuery as pq
import random
from bs4 import BeautifulSoup
import re

data = get_url('https://www.maomiav.com/assets/js/custom/config.js').text
maomi = re.findall('www.*?.com', data)[2]
r = get_url('https://'+maomi)
reditList = r.history
maomi=reditList[len(reditList)-1].headers["location"]
maomi = re.search('www.(.*?).com',maomi).group(1)


first_list=[
            'https://www.'+maomi+'.com/xiaoshuo/list-%E9%83%BD%E5%B8%82%E6%BF%80%E6%83%85',
            'https://www.'+maomi+'.com/xiaoshuo/list-%E4%BA%BA%E5%A6%BB%E4%BA%A4%E6%8D%A2',
            'https://www.'+maomi+'.com/xiaoshuo/list-%E6%A0%A1%E5%9B%AD%E6%98%A5%E8%89%B2',
            'https://www.'+maomi+'.com/xiaoshuo/list-%E5%AE%B6%E5%BA%AD%E4%B9%B1%E4%BC%A6',
            'https://www.'+maomi+'.com/xiaoshuo/list-%E6%83%85%E8%89%B2%E7%AC%91%E8%AF%9D',
            'https://www.'+maomi+'.com/xiaoshuo/list-%E6%80%A7%E7%88%B1%E6%8A%80%E5%B7%A7',
            'https://www.'+maomi+'.com/xiaoshuo/list-%E6%AD%A6%E4%BE%A0%E5%8F%A4%E5%85%B8',
            'https://www.'+maomi+'.com/xiaoshuo/list-%E5%8F%A6%E7%B1%BB%E5%B0%8F%E8%AF%B4',
             ]

def second(url):#小说页解析
    data=get_url(url).text
    data = pq(data)
    data = data('.content').text()
    return data

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
    deta=second(url)
    return deta

def generate(): #获取随机页码
    i=random.randint(0,7)
    j=random.randint(1,30)
    if j == 1:
        return first_list[i]+'.html'
    else:
        return first_list[i]+'-'+str(j)+'.html'

def start_xiao():   #开始
    msg = xiao(generate())
    return msg

print(start_xiao())




