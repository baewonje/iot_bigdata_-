import re
original_text = """ a1 qweqweqw
123123 sadasdasd
zxczx zxczxczxc
adad ewfrwrwerwer
"""

p = re.compile('[a-zA-Z0-9][0-9]')
m = p.match(original_text)
print(m)