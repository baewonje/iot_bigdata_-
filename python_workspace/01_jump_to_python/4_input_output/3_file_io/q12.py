class Calulator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val

class UpgradeCaluator(Calulator):
    def minus(self,val):
        self.value -=val

cal = UpgradeCaluator()
cal.add(10)
cal.minus(7)

print(cal.value)