import re

p = re.compile('(blue|white|red)')
m = p.sub('colour', 'blue socks and red shoes')
print(m)
print(p.sub('colour', 'blue sock and red shoes',count=1))
print(p.sub('colour', 'blue sock and red shoes',count=2))
print(p.subn('colour', 'blue sock and red shoes'))
