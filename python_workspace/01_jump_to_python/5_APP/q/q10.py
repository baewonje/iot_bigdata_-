class Calculator:
    def __init__(self,number):
        self.number = number
        self.total = 0
    def sum(self):
        for i in self.number:
            self.total += i
        print(self.total)
    def avg(self):
        average = self.total/len(self.number)
        print(average)

cal1 = Calculator([1,2,3,4,5])
cal1.sum()
cal1.avg()
cal2 = Calculator([6,7,8,9,10])
cal2.sum()
cal2.avg()