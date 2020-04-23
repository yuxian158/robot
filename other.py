from picture import get_url
from pyquery import PyQuery as pq
import requests
import base64
def analysis(): #一言
    url = 'https://hitokoto.cn/'
    data=get_url(url).text
    doc=pq(data)
    return (doc('#hitokoto .word').text()+doc('#hitokoto .author').text())
def sec_wea(city):
    appkey='d57f9b847e352341adcf6f9ea6b95f59'
    param={
            "city" : city, #要查询的城市，如：温州、上海、北京
            "key" : appkey
           }
    req=requests.get('http://apis.juhe.cn/simpleWeather/query',params=param)
    # req.encoding('UTF-8')
    return req.json()
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


data = {'city':'南京'}
rul = 'https://v1.alapi.cn/api/tianqi/now'
req = requests.post(rul,data=data)
data = req.json()['data']
print('日期：',data['week'])
print('城市：',data['city'])
print('天气：',data['wea'],'温度范围',data['tem1'],'~',data['tem2'],'当前温度:',data['wea'])
print('风力')
