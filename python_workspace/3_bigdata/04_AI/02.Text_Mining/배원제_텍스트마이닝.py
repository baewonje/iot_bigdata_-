# 과제 수행 목표 : 한글 text를 대상으로 한 텍스트마이닝 적용
# 데이터 출처: https://news.naver.com/
# 텍스트 데이터:
# 예측 항목: 실시간 헤드라인 뉴스
# 어휘 분류 기준:Step1] 주요 어휘 분석
# 검찰 (26)
# 대통령 (18)
# 뉴스 (13)
# 개혁 (13)
# 법무부 (13)
# 역대 (12)
# 최저 (12)
# 경제 (12)
# ...
# 판정 기준: konlpy.tag

import codecs
# from konlpy.tag import Twitter
from konlpy.tag import Okt
import requests # 웹 페이지의 HTML을 가져오는 모듈
from bs4 import BeautifulSoup# HTML을 파싱하는 모듈
import urllib.request

#웹 페이지를 가져온뒤 BeautifulSoup 객체로 만듦
response = urllib.request.urlopen("https://news.naver.com/")
soup = BeautifulSoup(response, 'html.parser')

# table = soup.find('ul',{'class':'type06_headline'})

okt = Okt()
word_dic = {}
lines = soup.findAll('script', attrs={'type':'text/javascript'})
for line in lines:
    malist = okt.pos(str(line),norm=True, stem=True)
    for word in malist:
        if word[1] == "Noun": # 명사 확인하기 ---(*3)
            if not (word[0] in word_dic):
                word_dic[word[0]] = 0
            word_dic[word[0]] += 1 # 카운트 하기

# 많이 사용된 명사출력하기 ---(*4)
keys = sorted(word_dic.items(), key=lambda x:x[1], reverse=True)
print('\nStep1] 주요 어휘 분석')
for word,count in keys[:50]:
    print("{0} ({1})".format(word,count))
print()
