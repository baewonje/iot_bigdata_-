import re

email_list = "park@naver.com","kim@daum.net","lee@myhome.co.kr"

p = re.compile('.*[@].*[.](?=com|net$).*$')

for email_name in email_list:
    print(p.search(email_name))

