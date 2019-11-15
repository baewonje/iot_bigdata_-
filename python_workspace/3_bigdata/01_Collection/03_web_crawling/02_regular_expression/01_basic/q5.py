import re

p = re.compile('ab{3}')
m = p.match('abbbsdffsdfsdfsd')
print(m)