import re

p = re.compile('(ABC)+')
m = p.search('ABCABCABC OK?')
print(m)

print(m.group(0))

p = re.compile('(김혜경)+')
m = p.search('김혜경김혜경 OK?')
print(m)
print(m.group(0))

m = p.search('김혜경김혜경 우리 막내 김혜경!')
print(m)
print(m.group(0))
print(m.group(1))

p = re.compile(r'\w+\s+\d+[-]\d+[-]\d+')
m = p.search('park 101-1231-1231')
print(m)

p = re.compile(r'\w+\s+\d+[-]\d+[-]\d+')
m = p.search('park 1011-12111131-1231')
print(m)

p = re.compile(r'(\w+)\s+\d+[-]\d+[-]\d+')
m = p.search('park 101111-1231-1231')
print(m.group(1))
