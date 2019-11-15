import re

phone_list = """
park 111-1111-1111
kim 222-2222-2222
lee 333-3333-3333
"""

p = re.compile("(\d{3})[-](\d{4})[-](\d{4})")
print(p.sub("\g<1>-\g<2>-####",phone_list))