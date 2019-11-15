import re

p = re.compile('\w+z+\w')
m =p.findall('azs df szd fsd,,,a.')
print(m)