import re

p = re.compile('ca{3}t')
m = p.match('1')
print(m)
m = p.match('ct')
print(m)
m = p.match('caat')
print(m)
m = p.match('caaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaat')
print(m)

p = re.compile('goo{2}gle')
m = p.match('gooooooooooooooooooooooooooooogle')
print(m)
m = p.match('gooogle')
print(m)

p = re.compile('ca{,2}t')
m = p.match('cat')
print(m)
m = p.match('caat')
print(m)

p = re.compile('ca{1,5}t')
m = p.match('cat')
print(m)
m = p.match('caaaaat')
print(m)

p = re.compile('ca{5,}t')
m = p.match('cat')
print(m)
m = p.match('caaaaaaat')
print(m)


p = re.compile('ca?t')
m = p.match('cat')
print(m)
m = p.match('ct')
print(m)
m = p.match('caat')
print(m)