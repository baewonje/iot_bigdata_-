import urllib.request
from bs4 import BeautifulSoup
import re

html = urllib.request.urlopen('http://web.kma.go.kr/aboutkma/intro/daegu/index.jsp')
soup=BeautifulSoup(html, 'html.parser')

tags=soup.find_all('tr')
rain_list = []
temperature_list = []
weather_list = []

title=re.compile('PD_none" title="(\w+)"')
for tag in tags:
    try:
        if tag.th.string == '날씨':
            for td in tag:
                t = title.search(str(td))
                try:
                    if td.attrs['class'][0] in "bg_tomorrow":         break
                except: pass
                if t:
                   weather_list.append(t.group(1))
            break
    except: pass
print(weather_list)

title=re.compile('<td class="">(\d+)</td>')
for tag in tags:
    try:
        if tag.th.string == '강수확률(%)':
            for td in tag:
                t = title.search(str(td))
                try:
                    if td.attrs['class'][0] == "bg_tomorrow":         break
                except: pass
                if t:
                   rain_list.append(t.group(1))
            break
    except: pass
print(rain_list)

title=re.compile('<p class="plus">(\d+)</p></td>')
for tag in tags:
    try:
        if tag.th.string == '기온(℃)':
            for td in tag:
                t = title.search(str(td))
                try:
                    if td.attrs['class'][0] == "bg_tomorrow": break
                except: pass
                if t:
                   temperature_list.append(t.group(1))
            break
    except: pass
print(temperature_list)


