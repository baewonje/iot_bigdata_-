import re

p = re.compile('\w+')
m =p.match('aaaaaaaaaaaaa')
print(m)