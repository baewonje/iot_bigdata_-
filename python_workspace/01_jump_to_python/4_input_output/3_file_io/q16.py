class Restaurant:
    def __init__(self,name,type):
        self.restaurant_name = name
        self.custine_type = type
        self.number_served = 0

    def describe_restaurant(self):
        print("저희 레스토랑 명칭은 %s 이고 %s 전문점입니다."%(self.restaurant_name,self.custine_type))
    def open_restaurant(self):
        print("저희 %s 레스토랑 오픈했습니다."%self.restaurant_name)
    def reset_number_served(self):
        print("손님 카운팅을 0으로 초기화 하였습니다.")
        self.number_served = 0
    def increment_number_served(self,number_served):
        print("손님 %d명 들어오셨습니다. 자리를 안내해 드리겠습니다." % number_served)
        self.number_served += number_served
    def check_customer_number(self):
        print("지금까지 총 %d명 손님께서 오셨습니다."% self.number_served)

    def __del__(self):
        print("%s 레스토랑 문 닫습니다." % self.restaurant_name)

list=[]
name,type = input("레스토랑 이름과 요리 종류를 선택하세요.(공백구분): ").split()
list = Restaurant(name, type)
list.describe_restaurant()
open = input("레스토랑을 오픈하시겠습니까?(y/n): ")
if open == 'y':
    list.open_restaurant()
    while True:
        number_served = (input("어서오세요. 몇명이십니까?(초기화:0입력,종료:-1,누적고객 확인:p):    "))
        if number_served == '0':
            list.reset_number_served()
        elif number_served == 'p':
            list.check_customer_number()
        elif number_served == '-1':
            break
        else:
            list.increment_number_served(int(number_served))
