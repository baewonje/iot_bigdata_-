class calculater:
    def __init__(self):
        self.result=0


    def add(self,num):
        self.result += num
        return self.result

cal1 = calculater()
cal2 = calculater()
cal3 = calculater()

print(cal1.add(1))
print(cal1.add(2))
print(cal2.add(3))
print(cal2.add(4))
print(cal3.add(5))
print(cal3.add(6))
