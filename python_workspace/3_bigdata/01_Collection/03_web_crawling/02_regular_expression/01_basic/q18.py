import re

p = re.compile('\d{1,3}.')
m =p.findall('Exercises number 1, 12, 13, and 345 are important')
print(m)