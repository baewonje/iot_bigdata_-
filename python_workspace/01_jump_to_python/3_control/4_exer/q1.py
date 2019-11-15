#coding=cp949

age = 0
age1 = 2000
age2 = 3000
age3 = 4000
age4 = 5000
age5 = "무료"


age= int(input("나이를 입력하세요. "))

if 0<= age <= 3:
    print("요금은 %s입니다."%age5)
elif 4 <= age <= 13:
    print("요금은 %d원입니다."%age2)
elif  14 <= age <= 18:
    print("요금은 %d원입니다."%age3)
elif  19 <= age <= 65:
    print("요금은 %d원입니다."%age4)
elif age > 65:
    print("요금은 %s입니다."%age5)
