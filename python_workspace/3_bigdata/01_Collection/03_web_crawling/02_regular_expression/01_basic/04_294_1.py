import re

p = re.compile('[^a-zA-Z0-9_]')
m = p.match('@')
print(m)
m = p.match('a')
print(m)

p = re.compile('[0-9]')
m = p.match('asd')
print(m)

p = re.compile('^')
m = p.match('^')
print(m)
