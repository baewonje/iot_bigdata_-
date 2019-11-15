import re
original_text = 'life is too short'
# original_text = '#### ## ### short'
p = re.compile('[a-z]+')
m = p.match(original_text)
print(m)

m = p.search(original_text)
print(m)

m = p.findall(original_text)
print(m)

m = p.finditer(original_text)
print(m)

match_list = p.findall(original_text)

for match_element in match_list:
    print(match_element)
