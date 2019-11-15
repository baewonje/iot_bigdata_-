import re

p = re.compile('(ABC)+')
m = p.search('ABCABCABCABCABC OK?')
print(m)
print(m.group(0))