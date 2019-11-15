import urllib.request
import datetime
import json
import time



access_key = "WjF8b7ubtxqL4v%2BGGDiKHmlzdYuzak5z548vypCpbJXcB3TCRFmBo6VwfregwjGpyAh11Skos%2FIwufWMUB827g%3D%3D"

def get_Request_URL(url):
    # (1) 기상 정보(동네예보정보 조회 서비스) / (2) 통합대기환경 정보(대기오염정보 조회 서비스)
    req = urllib.request.Request(url) # request 날리는 함수

    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print("[%s] Url Request Success" %(datetime.datetime.now()))
            return response.read().decode('UTF-8')
    except Exception as e:
        print(e)
        print("[%s] Error for URL : %s" %(datetime.datetime.now(), url))
        return None

def get_Weather_URL(yyyymmdd,day_time):
    x_coodinate = "89"
    y_coodinate = "91"
    # (1)기상 정보(동네예보정보 조회 서비스) request 보내기 전, url 만드는 함수
    end_point = "http://newsky2.kma.go.kr/service/SecndSrtpdFrcstInfoService2/ForecastTimeData"  # ForecastTimeData 서비스를 이용할 것

    parameters = "?_type=json&ServiceKey="+ access_key # 메뉴얼을 보고 요청 메세지를 완성할 것
    parameters += "&base_date="+yyyymmdd
    parameters += "&base_time="+str(day_time)
    parameters += "&nx="+ x_coodinate
    parameters += "&ny="+ y_coodinate

    url = end_point + parameters
    retData = get_Request_URL(url)
    print(retData)
    if (retData == None):
        return None
    else:
        return json.loads(retData)

def get_Realtime_Weather_Info(): #시간 정보를 보정하여 Make_Weather_Json() 을 호출한다.
    if int(time.strftime('%M')) < 30 :
        an_hour_later =str(int(datetime.datetime.today().hour)-1)
        day_time = an_hour_later
        return day_time
    else:
        now_time=time.strftime('%H%M', time.localtime(time.time()))
        day_time = now_time
        return day_time

def main():
    json_weather_result = []
    # (1) 기상 정보(동네예보정보 조회서비스) json 파일을 생성하는 함수
    yyyymmdd=time.strftime('%Y%m%d',time.localtime(time.time()))
    jsonData = get_Weather_URL(yyyymmdd,get_Realtime_Weather_Info)
    index=0
    for i in jsonData['response']['body']['items']['item']:
        # jsonData를 parsing 하여 json_weather_result에 저장된 예제 샘플을 참고하여 데이터를 저장한다.
        if(jsonData['response']['header']['resultMsg']=='OK'):
            ymd = jsonData['response']['body']['items']['item'][index]["baseDate"]
            day_time = jsonData['response']['body']['items']['item'][index]["baseTime"]
            nx = jsonData['response']['body']['items']['item'][index]["nx"]
            ny = jsonData['response']['body']['items']['item'][index]["ny"]
            category = jsonData['response']['body']['items']['item'][index]["category"]
            fcstDate = jsonData['response']['body']['items']['item'][index]["fcstDate"]
            fcstTime = jsonData['response']['body']['items']['item'][index]["fcstTime"]
            fcstValue = jsonData['response']['body']['items']['item'][index]["fcstValue"]
            index+=1

        json_weather_result.append([ymd,day_time,category,fcstDate,fcstTime,fcstValue,nx,ny])
    with open('동구_신암동_초단기예보조회_%s%s.json'%(ymd,day_time), 'w', encoding='UTF-8') as outfile:
        retJson = json.dumps(json_weather_result, indent = 4, sort_keys=True,ensure_ascii=False)

        outfile.write(retJson)

    print('동구_신암동_초단기예보조회_%s_%s.json SAVED'%(ymd,day_time))


if __name__ == '__main__':
    main()



