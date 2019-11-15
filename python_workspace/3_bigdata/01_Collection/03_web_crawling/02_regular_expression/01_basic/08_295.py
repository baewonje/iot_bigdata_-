import re

p = re.compile('ca*t')
m = p.match('1')
print(m)
m = p.match('ct')
print(m)
m = p.match('cat')
print(m)
m = p.match('caaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaat')
print(m)

p = re.compile('goo*gle')
m = p.match('gooooooooooooooooooooooooooooogle')
print(m)