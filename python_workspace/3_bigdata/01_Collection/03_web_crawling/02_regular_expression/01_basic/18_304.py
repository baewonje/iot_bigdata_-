import re

p = re.compile('[a-z]', re.I)
m = p.match('python')
print(m)
m = p.match('Python')
print(m)
m = p.match('PYTHON')
print(m)
