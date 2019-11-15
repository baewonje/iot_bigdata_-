import re

p = re.compile('\w+$')
m =p.match('azsdfszdfsd')
print(m)