import urllib.request
from bs4 import BeautifulSoup
import re


html = urllib.request.urlopen('http://web.kma.go.kr/aboutkma/intro/daegu/index.jsp')
soup=BeautifulSoup(html, 'html.parser')

tags=soup.find_all('tr')
rain_list = []
temperature_list = []
weather_list = []
total = 0



def weatherforecast():
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
    print("날씨")
    print(weather_list)

def rainfall():
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
    print("강수확률(%s)")
    print(rain_list)

def temperature():
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
    print("기온( C)")
    print(temperature_list)

def message():
    if '비' or '소나기' in weather_list:
        print("우산을 챙기세요.")
    elif '맑음' in weather_list:
        print('선크림을 바르세요')

def check(temperature_list):
    global total
    for i in range(0, len(temperature_list)):
        total = int(total)
        total += int(temperature_list[i])

    total = total / len(temperature_list)

    if total > 23:
        print("민소매티, 반바지, 반팔티, 원피스를 추천합니다.")
    elif 20 < total < 23:
        print("긴팔티,긴바지, 얇은 가디건을 추천합니다.")
    elif 16 < total < 20:
        print("맨투맨티, 얇은 가디건을 추천합니다.")
    elif 12 < total < 16:
        print("트렌치코트, 남방을 추천합니다.")
    elif 6 < total < 12:
        print("코트, 스웨터을 추천합니다.")
    elif total < 6:
        print("패딩, 스웨터, 두꺼운 바지를 추천합니다.")

def main():
    temperature()
    weatherforecast()
    rainfall()
    check(temperature_list)
    message()

if __name__ == '__main__':
    main()
