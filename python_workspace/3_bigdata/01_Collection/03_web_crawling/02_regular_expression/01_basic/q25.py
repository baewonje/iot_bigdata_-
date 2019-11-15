import re

url = """
2009-01-21
2012-12-12"""

p = re.compile('(\d{4})-(\d{2})-(\d{2})')
print(p.sub("\g<3>-\g<1>-\g<1>",url))
