class Restaurant:
    def __init__(self,name,type):
        self.restaurant_name = name
        self.custine_type = type

    def describe_restaurant(self):
        print("저희 레스토랑 명칭은 %s 이고 %s 전문점입니다."%(self.restaurant_name,self.custine_type))
    def open_restaurant(self):
        print("저희 %s 레스토랑 오픈했습니다. 어서오세요."%self.restaurant_name)
    def __del__(self):
            print("%s 레스토랑 문 닫습니다."%self.restaurant_name)
list=[]
for index in range(3):
    name,type = input("레스토랑 이름과 요리 종류를 선택하세요.(공백구분): ").split()
    list.append(name)
    list[index] = Restaurant(name, type)
    list[index].describe_restaurant()
    list[index].open_restaurant()
print("저녁 10시가 되었습니다.")
for index in range(3):
     del list[0]