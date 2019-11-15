#coding=cp949

age = []
money = 0
choice = 0
ticket = ["티켓1","티켓2"]
age1 = {'유아':'무료','어린이':'2000','청소년':'3000','성인':'5000','노인':'무료'}
dict_keys(['유아'])
prompt="""
1. 현금
2. 공원 전용 신용 카드
"""
while True:
    age=int(input("나이를 입력하세요. "))
    if 0 <= age <= 3:
        print("귀하는 %s등급이며 요금은 %s입니다."%(age1.key(0),age1['유아']))
        print("티켓을 발행합니다.")
        continue
    elif 4 <= age <= 13:
        print("귀하는 %s등급이며 요금은 %d입니다."%(age1.key(1),age1['어린이']))
    elif  14 <= age <= 18:    
        print("귀하는 %s등급이며 요금은 %d입니다."%(age1.key(2),age1['청소년']))
    elif  19 <= age <= 65:
        print("귀하는 %s등급이며 요금은 %d입니다."%(age1.key(3),age1['성인']))
    elif age > 65:
        print("귀하는 %s등급이며 요금은 %s입니다."%(age1.key(4),age1['노인']))
        print("티켓을 발행합니다.")
        continue
            
    choice = int(input(prompt))
    if choice == 1:
            money=int(input("요금을 입력하세요. "))
            if 4 <= age <= 13 and money>=age1['어린이']:
                print("감사합니다. 티켓을 발행하고 거스름돈 %d원을 반환합니다."%(money-(age1['어린이'])))
                if money < age1['어린이']:
                    print("%d원이 모자랍니다. 입력하신 %d원을 반환합니다."%((age1['어린이'])-money,money))
            elif 14 <= age <= 18 and money >= age1['청소년']:
                print("감사합니다. 티켓을 발행하고 거스름돈 %d원을 반환합니다."%(money-(age1['청소년'])))
                if money < age1['청소년']:
                    print("%d원이 모자랍니다. 입력하신 %d원을 반환합니다."%((age1['청소년'])-money,money))
            elif 19 <= age <= 65 and money>=age1['성인']:
                print("감사합니다. 티켓을 발행하고 거스름돈 %d원을 반환합니다."%(money-(age1['성인'])))
                if money < age1['성인']:
                    print("%d원이 모자랍니다. 입력하신 %d원을 반환합니다."%((age1['성인'])-money,money))
    elif choice == 2:
            result = [money2*0.9 for money2 in money1]
            if age >= 60:
                print("%d원이 결제 되었습니다. 티켓을 발행합니다." %(((money1[3])*0.9)*0.95))
            elif age>= 4:
                print("%d원이 결제 되었습니다. 티켓을 발행합니다." %((money1[3])*0.9))

    if 4<=age<=65:
            count +=1
            if count % 7 == 0 :
                if ticket >0:
                    print("축하합니다. 1주년 이벤트에 당첨 되었습니다. 여기 무료티켓을 발행합니다. 잔여 무료티켓 %d장"%(ticket-1))
                    ticket -=1
            elif count % 4 == 0:
                if year >0:
                    print("축하합니다. 연간 회원권 구매 이벤트에 당첨되셨습니다. 연간 회원 할인 티켓을 발행합니다. 잔여티켓 %d장"%(year-1))
                    year-=1


