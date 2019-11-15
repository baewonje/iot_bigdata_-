import urllib.request
client_id = "asd"
client_secret = "asd"
default_str ="안녕하세요. 홍길동입니다 안녕!"
emotion_str="안녕하세요.?안녕하세요"
encText = urllib.parse.quote(default_str)
data = "speaker=jinho&speed=0&text=" + encText;
url= "https://openapi.naver.com/v1/voice/tts.bin"
request = urllib.request.Request(url)
request.add_header("X-naver-Client-Id",client_id)
request.add_header("X-naver-client-scret",client_secret)
response = urllib.request.urlopen(request, data=data.encode('utf-8'))
rescode = response.getcode()
if(rescode==200):
    print("TTs mp3 저장")
    response_body = response.read()
    with open('11112.mp3','wb') as f:
        f.write(response_body)
else:
    print("Error code:" + response)
