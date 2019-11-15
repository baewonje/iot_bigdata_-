import re

p = re.compile(r'(?P<name>\w+)\s+((\d+)[-]\d+[-]\d)+')
p = re.compile(r'(?P<name>\w+)\s+(?P<first_number>\d+)[-]\d+[-]\d+')
p = re.compile(r"""     # 원문이 park 111-2222-3333 일 경우에 
(?P<name>\w+)\s+        # 이름이 매칭이 되는 정규식: park 매치
(?P<first_number>\d+)   # 첫번째 전화번호 그룹: 111 매치
[-]                     # 첫번째 전화번호 그룹 뒤에 반드시 '-' 문자가와야함
(?P<second_number>\d+)  # 두번째 전화번호 그룹 : 2222 매치
[-]                     # 두번째 전화번호 그룹 뒤에 '-'
(?P<third_number>\d+)   # 세번째 전화번호 그룹 : 3333
""",re.VERBOSE)
m = p.search('park 111-2222-3333')
print(m.group('name'))
print(m.group('first_number'))
print(m.group('second_number'))
print(m.group('third_number'))
