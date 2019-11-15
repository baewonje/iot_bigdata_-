import os

print(os.getcwd())
# 환경변수 PATH에 잡혀있는 실행 파일은 실행파일명만 입력하면 된다.

# os.system("dir")
# 실행 파일이 실행인자가 유효하다면 적용할 수 있다.
# os.system("notepad my_info.txt")
# os.system("notepad ./info_data/my_info.txt")
# os.chdir('./info_data')
# os.system("notepad my_info.txt")
# PATH에 잡혀있지 않는 실행파일은full PATH를 입력해야한다.
# 여기서 PATH에 공백문자가 있다면 아래와 같이 실행파일을 앞뒤로 \" 를 넣어주어야 한다.
# os.system("\"C:\Program Files (x86)\Microsoft Office\Office14\POWERPNT.EXE\"")
# FULL PATH를 요구하는 실행파일이 실행인자가 유효하다면 이어서 실행인자를 넣을 수 있다.
# system 명령어는 병렬로 수행되지 않고 순차적으로 수행한다. 즉 위의 실행 프로그램이
# 종료되어야 아래 system명령어가 수행 된다.
# os.system("\"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe\" https://cafe.naver.com/iotbigdata")

f = os.popen("dir")
print(f.read())