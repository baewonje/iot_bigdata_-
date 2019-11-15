import urllib.request
import datetime
import json
import time
import csv
output_file = '대구광역시_동구_단기예보5.csv'

access_key = 'pUzCOfH0tRU0daYQ47fcsGrDUtqRi9%2F5tRBwHn980XHUpP8C4oWuyh4JK2DIjgoDqzn%2FGS51KnhRrXZVEdrWfg%3D%3D'
x_coodinate = "89"
y_coodinate = "91"

csv_out_file = open(output_file, 'w', newline='')
filewriter = csv.writer(csv_out_file)
header_list = ['baseDate','baseTime','category','fcstDate','fcstTime','fcstValue','nx','ny']
filewriter.writerow(header_list)

def get_Requrest_URL(url):
    req = urllib.request.Request(url)

    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print("[%s] Url:%s => Request Success" % (datetime.datetime.now(), url))
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print("[%s] Error for URL: %s" % (datetime.datetime.now(), url))
        return None

def get_Weather_URL(day_time):
    base_date = time.strftime('%Y%m%d', time.localtime(time.time()))
    end_point = "http://newsky2.kma.go.kr/service/SecndSrtpdFrcstInfoService2/ForecastTimeData"
    parameters = ("?base_date=%s&base_time=%s&nx=%s&ny=%s&_type=json&numOfRows=100&serviceKey=%s") \
                 %(base_date,day_time,x_coodinate,y_coodinate,access_key)

    url = end_point + parameters
    retData = get_Requrest_URL(url)
    if (retData == None):
        return None
    else:
        return json.loads(retData)

def Make_Weather_Json(day_time):
    jsonData = get_Weather_URL(day_time)
    for data in jsonData['response']['body']['items']['item']:
        baseDate = data["baseDate"]
        baseTime =data["baseTime"]
        category = data["category"]
        fcstDate = data["fcstDate"]
        fcstTime = data["fcstTime"]
        fcstValue = data["fcstValue"]
        nx = data["nx"]
        ny = data["ny"]

        row_list = [baseDate,baseTime,category,fcstDate,fcstTime,fcstValue,nx,ny]
        filewriter.writerow(row_list)
        # json_weather_result.append({baseDate,baseTime,category,fcstDate,fcstTime,fcstValue,nx,ny})


    yyyymmdd = time.strftime('%Y%m%d', time.localtime(time.time()))
    print('동구_신암동_초단기예보조회_%s%s.json' % (yyyymmdd, day_time))

def get_Realtime_Weather_Info():
    if time.localtime().tm_min in range(0,31):
        real_time = str(time.localtime().tm_hour - 1) + '59'
    else:
        real_time = time.strftime('%H%M', time.localtime(time.time()))
    if len(real_time) == 3:
        real_time = '0' + real_time
    Make_Weather_Json(real_time)

get_Realtime_Weather_Info()
