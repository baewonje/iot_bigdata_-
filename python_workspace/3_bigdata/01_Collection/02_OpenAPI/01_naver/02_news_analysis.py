import json
import operator

news_domain_all_list = []
domain_info_list = []
num_of_corrupted_data=0

with open("아베_naver_news.json", encoding="utf-8") as json_data:
    json_data_load = json.load(json_data)
    json_data_string = json.dumps(json_data_load)
    jsonResult = json.loads(json_data_string)
print("데이터 분석을 시작합니다..")
dict1 ={}

truee = 0
falsee = 0
for org in jsonResult:
    domain = org['org_link']
    if domain:
        domain1 = domain.split('/')
        truee = truee+1
        if domain1[2] in dict1.keys():
            dict1[domain1[2]] = dict1[domain1[2]]+1
        else:
            dict1[domain1[2]] = 1
            news_domain_all_list = news_domain_all_list+[domain1[2]]
    else:
        falsee = falsee+1
print(falsee)
print(truee)

news_domain_all_list = set(news_domain_all_list)
print(len(news_domain_all_list))

sortedArr = sorted(dict1.items(), key=operator.itemgetter(1), reverse=True)

for i in range(len(sortedArr)):
    print(f'>> {sortedArr[i][0]}: {sortedArr[i][1]}건')