class FourCal:
    # first = 0
    # second = 0 # 중간에 멤버 변수를 정의할 수 있어도 명시적으로 클래스
                 # 멤버 변수를 class 다음에 지정하는 것은
                    # 프로그램 유지보수와 가독성에 더 좋다고 볼 수 있다.
    def setdata(self,first, second):
        self.first = first # 멤버 변수가 없음에도 객체생성이후에
                            # 클래스의 멤버변수를 생성하는 것이 가능하다.
        self.second = second

    def print_number(self):
        print("first: %d, second: %d"%(self.first,self.second))
#         self를 사용하지 않으면 멤버함수에서 사용하는 지역변수로 인식한다.
#           따라서 아래 코드는 빌드시 에러를 발생하게 된다.
#           pritn("first: %d, second : %d"%(firse,second))

# a = FourCal(1,2) # 2개의 인자를 갖는 생성자가 없으므로 에러를 발생한다.
a= FourCal()
a.setdata(1,2) # 객채 생성이후의 멤버 변수 값을 설정할 때 사용한다.
a.print_number()
print(id(a.first))

b = FourCal()
b.setdata(3,2)
b.print_number()
print(id(b.first))

