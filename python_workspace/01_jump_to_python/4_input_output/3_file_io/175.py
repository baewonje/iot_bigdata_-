f = open("새파일.txt",'r',encoding='UTF-8')
data = f.read()
print(data) #아스키 모드 파일을 prnt 함수로 읽을 경우에
            #줄바꿈 현상 이 일어날 수 있다.

f.close()