import re

p = re.compile('ab*')
m = p.match('abbb')
print(m)