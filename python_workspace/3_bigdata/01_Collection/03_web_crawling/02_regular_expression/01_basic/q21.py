import re

original_text = ['exercises']

for p in original_text:
    p = re.compile(p)
    m =p.findall('Python exercises, PHP exercises, C# exercises')
    print(m)
