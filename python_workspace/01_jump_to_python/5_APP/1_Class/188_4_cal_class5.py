class FourCal:
    def setdata(self,first, second):
        self.first = first # 멤버 변수가 없음에도 객체생성이후에
        self.second = second
    def add(self):
        result = self.first + self.second
        return result

    def print_number(self):
        print("first: %d, second: %d"%(self.first,self.second))

a= FourCal()
a.setdata(1,2) # 객채 생성이후의 멤버 변수 값을 설정할 때 사용한다.
a.print_number()
print(a.add())
print("first: %d, second: %d"%(a.first,a.second))
print(a.first+a.second)
# 위와 같이 python의 모든 클래스의 멤버 변수, 함수는 속성이 public,이라
# 외부에서 모두 접근이 가능하다.
# 하지만 클래스의 멤버 변수에 대해서 설정하는 것은
#  클래스 정의시 멤버변수 정의, 생성자, setxxx()함수로 정의 및 수정을 하는 것이
# 객체지향 프로그래밍에 가깝다.
temp = [1,2,3,4]
temp.__class__
# 객체지향언어에서의 private 개념은 __멤버변수__.
