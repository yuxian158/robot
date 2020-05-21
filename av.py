from pyquery import PyQuery as pq
from picture import get_url
import re

def av(avnum):
    inform = []
    data = get_url('https://www.javbus.com/'+avnum)
    if data.status_code==200:
        data = data.text
        doc = pq(data)
        items = doc('.col-md-9')
        png = items.find('a').attr('href')
        name = items.find('img').attr('title')
        inform.append(png)
        inform.append(name)
        gid = re.search('gid.=.(\d{11})', data, re.S)
        uc = re.search('uc.=.(\d)', data, re.S)
        img = re.search('var.img.=.\'(.*)\';', data, re.S)
        url = 'https://www.javbus.com/ajax/uncledatoolsbyajax.php?gid=' + gid.group(1) + '&lang=zh&img=' + img.group(
            1) + '&uc=' + uc.group(1) + '&floor=413'
        href = get_url(url).text
        data = pq(href)
        datas = data('tr').items()
        for data in datas:
            inform.append(data('tr').text() + '   ' + data('tr a').attr('href'))
        return inform
    else:return inform
# data='番号ABP-417'
# # print(re.match('番号(.*?-.*[^\D])',data))
# # print(re.search('番号(.*?-.*[^\D])',data))
# # if re.match('番号(.*?-.*[^\D])', data):
# #     mags = av(re.search('番号(.*?-.*[^\D])', data).group(1))
# #     print(mags)