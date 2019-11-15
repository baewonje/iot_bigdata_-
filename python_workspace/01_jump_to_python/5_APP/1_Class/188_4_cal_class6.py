class FourCal:
    def setdata(self,first, second):
        self.first = first # 멤버 변수가 없음에도 객체생성이후에
        self.second = second

    def add(self):
        result = self.first + self.second
        return result

    def mul(self):
        result = self.first - self.second
        return result

    def sub(self):
        result = self.first * self.second
        return result

    def div(self):
        result = self.first / self.second
        return result

    def print_number(self):
        print("first: %d, second: %d"%(self.first,self.second))

a= FourCal()
b= FourCal()
a.setdata(4,2)
a.setdata(3,8)# 객채 생성이후의 멤버 변수 값을 설정할 때 사용한다.
a.print_number()
b.print_number()
print(a.add())
print(a.mul())
print(a.sub())
print(a.div())
print(b.add())
print(b.mul())
print(b.sub())
print(b.div())
