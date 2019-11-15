#coding=cp949

age = 0
age1 = "유아"
age2 = "어린이"
age3 = "청소년"
age4 = "성인"
age5 = "노인"
money= "무료"
money1=2000
money2=3000
money3=5000

while True:
    age=int(input("나이를 입력하세요. "))
    if 0 <= age <= 3:
        print("귀하는 %s등급이며 요금은 %s입니다."%(age1,money))
        break
    elif 4 <= age <= 13:
        print("귀하는 %s등급이며 요금은 %s입니다."%(age2,money1))
        break
    elif  14 <= age <= 18:
        print("귀하는 %s등급이며 요금은 %s입니다."%(age3,money2))
        break
    elif  19 <= age <= 65:
        print("귀하는 %s등급이며 요금은 %s입니다."%(age4,money3))
        break
    elif age > 65:
        print("귀하는 %s등급이며 요금은 %s입니다."%(age5,money))
        break
    else:
        print("다시 입력하세요.")
