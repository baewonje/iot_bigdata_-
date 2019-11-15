import json
import urllib.request
import datetime
import math
from operator import itemgetter

# 서비스명: 관광자원통계서비스
access_key =["pUzCOfH0tRU0daYQ47fcsGrDUtqRi9%2F5tRBwHn980XHUpP8C4oWuyh4JK2DIjgoDqzn%2FGS51KnhRrXZVEdrWfg%3D%3D","WjF8b7ubtxqL4v%2BGGDiKHmlzdYuzak5z548vypCpbJXcB3TCRFmBo6VwfregwjGpyAh11Skos%2FIwufWMUB827g%3D%3D","OZvrnW3R3erL3CkQFH%2F7%2FNAfDo3U2nLKGToS3jta82kKaLh6LpnGqChjuAnzDvSLtdQaDjNniiIOX1PrSJuhUA%3D%3D"]
def get_request_url(url):
    req = urllib.request.Request(url)

    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print("[%s] Url Request Success"% datetime.datetime.now())
            return response.read().decode('UTF-8')
    except Exception as e:
        print(e)
        print("[%s] Error for URL:%s"%(datetime.datetime.now(),url))
        return None

# [CODE 1]
def getNatVisitor(yyyymm,nat_cd,ed_cd):
    key_num = 0
    end_point="http://openapi.tour.go.kr/openapi/service/EdrcntTourismStatsService/getEdrcntTourismStatsList"

    parameters ="?_type=json&serviceKey="+access_key[key_num]
    parameters += "&YM="+yyyymm
    parameters += "&NAT_CD="+nat_cd
    parameters += "&ED_CD="+ed_cd

    url =end_point+parameters

    retData = get_request_url(url)

    if(retData == None):
        end_point = "http://openapi.tour.go.kr/openapi/service/EdrcntTourismStatsService/getEdrcntTourismStatsList"
        parameters = "?_type=json&serviceKey=" +access_key[key_num]
        parameters += "&YM=" + yyyymm
        parameters += "&NAT_CD=" + nat_cd
        parameters += "&ED_CD=" + ed_cd

        url = end_point + parameters

        retData = get_request_url(url)
        key_num +=1
    else:
        return json.loads(retData)


def main():
    jsonResult = []
    # 중국:112/일본:130/미국:275
    f =open('national_code_selected.txt','r',encoding='UTF-8-sig')
    code_list = f.readlines()
    f.close()
    count=0

    ed_cd = "E"
    nStartYear = 2011
    nEndYear = 2019
    for i in code_list:
        national_code = code_list[count][0:3]
        national_visit = 0
        for year in range(nStartYear,nEndYear):
            for month in range(1,13):
                yyyymm = "{0}{1:0>2}".format(str(year),str(month))
                jsonData = getNatVisitor(yyyymm,national_code,ed_cd)

                if(jsonData['response']['header']['resultMsg']=='OK'):
                    krName = jsonData['response']['body']['items']['item']["natKorNm"]
                    krName = krName.replace(' ','')
                    iTotalVisit=jsonData['response']['body']['items']['item']["num"]
                    national_visit += iTotalVisit
                print('%s_%s:%s'%(krName,yyyymm,national_visit))
        jsonResult.append([krName,national_visit])

        cnVisit = []
        VisitYM = []
        index =[]

        i = 0

        for item in jsonResult:
            index.append(i)
            # cnVisit.append(item['visit_cnt'])
            # VisitYM.append(item['yyyymm'])
            i+=1
        count+=1

        jsonResult.sort(key=itemgetter(1), reverse=True)

    with open('%s(%s)_해외방문객정보_%d_%d.json'%(krName,national_code,nStartYear,nEndYear-1),'w',encoding='UTF-8') as outfile:
        retJson = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(retJson)

if __name__ == '__main__':
    main()

