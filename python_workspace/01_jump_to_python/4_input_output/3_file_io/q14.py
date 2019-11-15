class Restaurant:
    def __init__(self,name,type):
        self.restaurant_name = name
        self.custine_type = type

    def describe_restaurant(self):
        print("저희 레스토랑 명칭은 %s 이고 %s 전문점입니다."%(self.restaurant_name,self.custine_type))
    def open_restaurant(self):
        print("저희 %s 레스토랑 오픈했습니다. 어서오세요."%self.restaurant_name)
list=[]
name,type = input("레스토랑 이름과 요리 종류를 선택하세요.(공백구분): ").split()
list = Restaurant(name, type)
list.describe_restaurant()
list.open_restaurant()
