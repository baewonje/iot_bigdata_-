import re

p = re.compile('\w+\S*$')
m =p.match('asdfsdfsd,,,,,a.')
print(m)