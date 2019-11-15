#coding=cp949

i = 0
num = 1

while True:
    odd = int(input("홀수를 입력하세요.(0 <- 종료): "))
    if odd == 0:
        print("마름모 프로그램 출력을 이용해 주셔서 감사합니다.")
        break
    if odd != 0:
        num = 1
        while num<=odd:
            print("{0:^30}".format(num*('*')))
            num+=2
    if odd != 0:
        num = (odd)-2
        while num>=1:
            print("{0:^30}".format(num*('*')))
            num-=2