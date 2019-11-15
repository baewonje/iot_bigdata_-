a= "life is too short"

print(a.find('t'))
print(a.index('t'))

print("debug 1")
print(a.find('k')) # 'k' 가 없어도 프로그램 진행

print("debug 2")
print(a.index('k')) # 'k'가 없으면 프로그램 종료(runtime error 발생)

print("debug 3")
