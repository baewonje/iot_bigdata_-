import re

original_text = ['fox']

for p in original_text:
    p = re.compile(p)
    m =p.search('the quick brown fox jumps over the lazy dog')
    print(m,'\n',m.start(),m.end())
