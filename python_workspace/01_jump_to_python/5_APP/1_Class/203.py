class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def setdata(self, first, second):
        self.first = first  # 멤버 변수가 없음에도 객체생성이후에
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
        print("first: %d, second: %d" % (self.first, self.second))


class MoreFourcal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result

class SafeFourCal(FourCal):
    def div(self):      # 메서드 오버라이딩 : 자식 클래스에서 부모 클래스의 멤버함수를 재정의
        if self.second == 0:
            return 0
        else:
            return self.first / self.second

a = MoreFourcal(4,2)
print (a.pow())


a= SafeFourCal(4,0)
print(a.div())


