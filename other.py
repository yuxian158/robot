from picture import get_url
from pyquery import PyQuery as pq
import requests
import base64
import urllib.parse
from aip import AipSpeech

def analysis(): #一言
    url = 'https://hitokoto.cn/'
    data=get_url(url).text
    doc=pq(data)
    return (doc('#hitokoto .word').text()+doc('#hitokoto .author').text())

def sec_wea(city):
    data = {'city':city}
    rul = 'https://v1.alapi.cn/api/tianqi/now'
    req = requests.post(rul,data=data)
    data = req.json()['data']
    ser1='日期：'+data['week']+'\n'
    ser2='城市：'+data['city']+'\n'
    ser3='天气：'+data['wea']+'温度范围'+data['tem1']+'~'+data['tem2']+'当前温度:'+data['tem']+'\n'
    ser4='风向'+data['win']+'风力'+data['win_speed']+'\n'
    ser5='空气质量'+data['air_level']+'\n'
    ser6='小提示:'+data['air_tips']+'\n'
    return ser1+ser2+ser3+ser4+ser5+ser6
def ocr(data):
    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic"
    img = base64.b64encode(data)
    params = {"image": img}
    access_token = '24.4b8516022cb4eea87db68c28ed0d5e18.2592000.1589894370.282335-19504093'
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    result=''
    if response:
        for data in response.json()["words_result"]:
            result = result + data['words']
    return result

def voice_ocr(voice):
    APP_ID = '19504093'
    API_KEY = 'kGSWLgXvWtTRmR6939taVCA6'
    SECRET_KEY = 'jCLDKKL7PlmTl5sDPozAAvTHfg53GCdK'
    client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
    result=client.asr(voice, 'pcm', 16000, {
        'dev_pid': 1537,
                })
    return result

def search_title(title):
    res=[]
    last = urllib.parse.quote(title)
    data1 = requests.get('http://aip.s759n.cn/tiku?question='+last)
    res.append(data1.text)

    data2='question='+last
    url2='http://cx.icodef.com/wyn-nb'
    headers={
        'Content-type': 'application/x-www-form-urlencoded'
            }
    data2 = requests.post(url2,headers=headers,data=data2)
    res.append(data2.json()['data'])

    data3 = 'content='+last
    url3='http://test.vcing.top:81/japi.php?key=chaoxing&q='+last
    headers={
        'Content-type': 'application/x-www-form-urlencoded'
             }
    data3 = requests.post(url3,headers=headers,data=data3)
    res.append(data3.json()['answer'])
    results=''
    for i in res:
        results = results+i+'\n'
    return results
