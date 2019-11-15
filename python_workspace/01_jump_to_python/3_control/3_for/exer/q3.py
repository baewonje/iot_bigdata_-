#coding=cp949

num = 1
while True:
    odd = int(input("홀수를 입력하세요.(0 <- 종료): "))
    max = int(odd/2)

    if odd == 0:
        print("마름모 프로그램 출력을 이용해 주셔서 감사합니다.")
        break

    if odd != 0:
        print(' '+odd * "-"+' ')
        for star in range(0,max+1):
            print('|'+' '*(max-star) +'*'*((star*2)+1)+' '*(max-star)+'|')

    if odd != 0:
        for star in range(max-1, -1,-1):
            print('|'+' ' * (max - star)+ '*' * ((star * 2) + 1)+ ' ' * (max - star)+ '|')

    print(' '+ odd * "-"+ ' ')