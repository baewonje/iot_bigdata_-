import re

url = "www.naver.com/2009/01/21"

p = re.compile('/(\d{4})/(\d{2})/(\d{2})')
m = p.search(url)
print(m.group(1),m.group(2),m.group(3))
