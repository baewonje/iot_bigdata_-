import re

original_text = ['exercises']

for p in original_text:
    p = re.compile(p)
    m =p.finditer('Python exercises, PHP exercises, C# exercises')
    for a in m:
        print(a.start(),a.end())
