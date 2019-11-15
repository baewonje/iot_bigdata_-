import re

p = re.compile('[\d]') #[0-9]
m = p.match('1')
print(m)

p = re.compile('[\D]') #[^0-9]
m = p.match('1')
print(m)

p = re.compile('[\s]') #[\t\n\r\f\v]
m = p.match(' 1')
print(m)

p = re.compile('[\S]') #[^\t\n\r\f\v]
m = p.match(' 1')
print(m)

p = re.compile('[\w]') #[a-zA-Z0-9_]
m = p.match('a_12')
print(m)
m = p.match('D12')
print(m)
m = p.match('@')
print(m)

p = re.compile('[\W]') #[^a-zA-Z0-9_]
m = p.match('@')
print(m)
