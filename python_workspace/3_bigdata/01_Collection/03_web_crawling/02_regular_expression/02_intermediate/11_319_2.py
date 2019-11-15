import re

def hexrepl(match):
    "Return the hex string for a decimal number"
    value = int(match.group())
    return hex(value)

# p = re.compile(r"\d+")
p = re.compile('\d+')
print(p.sub(hexrepl,'call 65432 for printing. 12354 for user code.'))