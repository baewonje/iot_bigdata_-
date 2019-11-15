import re

p = re.compile('ab?')
m = p.match('ab')
print(m)