import re

p = re.compile(r"(?P<name>\w+)\s+(?P<phone>(\d+)[-]\d+[-]\d+)")
print(p.sub("\g<phone> \g<name>","park 111-2222-3333"))
print(p.sub("\g<2> \g<1>","park 111-2222-3333"))
