import re

p = re.compile('.') # 모든 문자클래스와 매칭이 된다.
                    # [] 문자열 클래스가 아닌 일반 문법으로 사용했을 경우
                    # '.'은  모든 문자를 의미하는 메타 문자로 사용된다.

m = p.match('.')
print(m)
m = p.match('1')
print(m)
m = p.match('#')
print(m)
m = p.match('/')
print(m)
m = p.match(' ')
print(m)
p = re.compile('a.b')
m = p.match('a b')
print(m)
m = p.match('a d')
print(m)

p = re.compile('a[.]b')
m = p.match('a b')
print(m)
m = p.match('a d')
print(m)
p = re.compile('a..[.]txt')
m = p.match('aad.txt')
print(m)
m = p.match('aa.txt')
print(m)

p = re.compile('...')
m = p.match('aad asdas')
print(m)

p = re.compile('...........')
m = p.match('aad ')
print(m)

