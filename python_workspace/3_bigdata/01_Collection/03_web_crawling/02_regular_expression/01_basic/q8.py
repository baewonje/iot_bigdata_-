import re

p = re.compile('[A-Z]+_[a-z]+$')
m =p.match('ASD_asddd')
print(m)