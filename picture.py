import requests
import random


def get_url(url):   #访问网站返回数据
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
        "Referer":url
              }
    response = requests.get(url, headers=headers)
    response.encoding='utf8'
    return response

def photo_l():
    url='https://mmslt1.com/tp/girl/Pantyhose/B-0'+str(random.randint(10,99))+'/'+str(random.randint(10,30))+'.jpg'
    data=get_url(url).content
    with open('gril.png', 'wb') as f:
        f.write(data)


def photo_2(num):
    pic_list=['zipai','yazhou','oumei','meitui','qingchun','luanlun','katong']
    page = pic_list[num]
    i = random.randint(1,20)
    if i < 10:
        we = '0'+str(i)
    else: we = str(i)
    url='https://mmtp1.com/maomao/'+page+'/'+str(random.randint(1,390))+'/'+we+'.jpg'
    data=get_url(url)
    if data.status_code == requests.codes.ok:
        return data.content
    else:return []
    # with open('yazhou.png', 'wb') as f:
    #     f.write(data)
