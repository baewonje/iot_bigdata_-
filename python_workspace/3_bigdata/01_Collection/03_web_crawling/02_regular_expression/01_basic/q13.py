import re

p = re.compile('\w+z+\w')
m =p.findall('aazs df szd fsd,,,a.')
print(m)