# coding: cp949

print("i eat %d apples." %3) # 포멧 스트링 결과를 바로 print

str="in addition, i eat %d bananas"%2
# 포멧 스트링은 문자열의 기능을 확장하는 파이썬 문법
print(str)

number = 4
print("Further more, i eat %d mangoes" %number)

number = "five"
print("moreover, i eat %s tangerine" %number)

number=0.25
print("at the end, ieat %s melon"%number)
# %s는 기본적으로 문자열을 지원하지만 모든 형에 사용할 수 있다.

print("my satisfaction rate for the dessert is 98%")
# 포멧 스트링 없이 단독으로 %s를 문자열로 사용하는 것은 가능

