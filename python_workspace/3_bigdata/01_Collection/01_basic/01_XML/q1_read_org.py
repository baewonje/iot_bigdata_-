from xml.etree.ElementTree import Element,parse
import xml.etree.ElementTree as ET


tree = ET.parse("students_info.xml")
note = tree.getroot()
counter = 0

menu='''
1. 요약 정보
2. 전체 데이터 조회
3. 종료
메뉴 입력: '''

def full_data():
    for child in note.getiterator():
        if child.tag == "student":
            for key in child.keys():
                if key == 'name':
                    print("* %s"%child.get(key))
                if key == 'sex':
                    print("- 성별: %s"%child.get(key))
            age_tag = child.find("age")
            print("- 나이: %s"%age_tag.text)
            major_tag = child.find("major")
            print("- 전공: %s"%major_tag.text)
            for language_value in child.getiterator("language"):
                if language_value:
                    for period_value in language_value.getiterator("period"):
                        print("> %s 학습기간:%s,level:%s" % (language_value.get("name"), period_value.get("value"), language_value.get("level")))

            print(" ")



while True:
    num= input(menu)
    if num == '1':
        pass
    elif num == '2':
        full_data()
    elif num == '3':
        break
