import re

p = re.compile('\d+\w*')
m =p.match('1azsdfszdfsd')
print(m)