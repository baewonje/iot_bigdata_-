import re

original_text = ['fox','dog','horse']

for p in original_text:
    p = re.compile(p)
    m =p.search('the quick brown fox jumps over the lazy dog')
    print(m)