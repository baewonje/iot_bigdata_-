import re

p = re.compile('[a-z]+_[a-z]+$')
m =p.match('asd_asd')
print(m)