import re

p = re.compile('\d{0,2}.')
m =p.match('123sdfszdfsd121312')
print(m)