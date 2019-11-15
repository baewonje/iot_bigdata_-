import urllib.request
from bs4 import BeautifulSoup

html = urllib.request.urlopen('https://movie.naver.com/movie/sdb/rank/rmovie.nhn')
soup = BeautifulSoup(html,'html.parser')

tags = soup.findAll('div', attrs={'class':'tit3'})
up_down = soup.find('img', attrs={'src':'https://ssl.pstatic.net/imgmovie/2007/img/common/bullet_r_r01.gif'})
body = soup.tbody
rank = soup.find('td',attrs={'class':'ac'}).img['alt']
range = soup.find('td',attrs={'class':'range ac'}).text
data= []

def data_correction(org_text): # 데이터 보정작업
    if org_text == '\xa0':
        return 'N/A' # Not Applicable
    return org_text
for td in tags:
    if td.find('a'):
        name = data_correction(td.find('a').text)
    if td.find('range ac'):
        range = data_correction(range.find('range ac').text)
    if td. find('ac'):
        rank = data_correction(td.find('td',attrs={'class':'ac'}).img['alt'])
    data.append([rank,name,range])
print(data)


