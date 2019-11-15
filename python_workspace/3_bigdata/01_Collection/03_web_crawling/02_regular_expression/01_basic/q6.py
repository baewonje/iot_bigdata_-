import re

p = re.compile('ab{2,3}')
m = p.match('abbbsdffsdfsdfsd')
print(m)