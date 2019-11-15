import re

p = re.compile('[a-c]')
m = p.match('apple')
print(m)
m = p.match('travel')
print(m)

p = re.compile('[a-z]')
m = p.match('travel')
print(m)

p = re.compile('[a-z]')
m = p.match('Travel')
print(m)

p = re.compile('[a-zA-Z]')
m = p.match('Travel')
print(m)

p = re.compile('[1-9]')
m = p.match('1st')
print(m)