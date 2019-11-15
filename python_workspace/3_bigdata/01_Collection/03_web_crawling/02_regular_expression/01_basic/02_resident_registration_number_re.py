import re

data = """
park 800804-1003040
kim 802923-1231111
"""

pat = re.compile("(\d{6})[-]\d{7}")
print(pat.sub("\g<1>-*******",data))

