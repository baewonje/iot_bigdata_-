from xml.etree.ElementTree import Element,parse
import xml.etree.ElementTree as ET


tree = ET.parse("students_info2.xml")
note = tree.getroot()
counter = 0


menu='''
1. 요약 정보
2. 입력
3. 조회
4. 수정
5. 삭제
6. 종료
메뉴 입력: '''

second_menu='''
1.개별 학생 조회
2.전체 학생 조회
3.상위 메뉴
메뉴 입력: '''

search_menu='''
1.ID
2.이름
3.나이
4.전공
5.컴퓨터 언어 명
6.컴퓨터 언어 학습 기간
7.컴퓨터 언어 레벨
8.상위메뉴
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

def summary_information():
    student_count = 0
    man_count = 0
    woman_count = 0
    major_count = 0
    language_count = 0
    senior_count = 0
    python_count = 0
    twenties_count = 0
    name2_dict={}
    name3_dict={}
    name4_dict={}
    thirties_count = 0
    fourties_count = 0
    for child in note.getiterator('student'):
        if child.get("name"):
            student_count += 1
        if child.get("sex") == "남":
                man_count += 1
        if child.get("sex") == '여':
                woman_count += 1
        if '컴퓨터' in child.find("major").text:
            major_count +=1
        if '통계' in child.find("major").text:
            major_count += 1
        if 20 <= int(child.find("age").text) < 30:
            name2_dict[child.get("name")] = child.findtext("age")
            twenties_count += 1
        if 30 <= int(child.find("age").text) < 40:
            name3_dict[child.get("name")] = child.findtext("age")
            thirties_count += 1
        if 40 <= int(child.find("age").text) < 50:
            name4_dict[child.get("name")] = child.findtext("age")
            fourties_count += 1

        for practicable in child.getiterator("practicable_computer_languages"):
            if practicable:
                language_count+=1
            if practicable.get("level") == '상':
                senior_count += 1
            if practicable.get("name") =='python':
                python_count += 1

    man_per= (man_count/student_count)*100
    woman_per = (woman_count/student_count)*100
    major_per = (major_count/student_count)*100
    language_per = (language_count/student_count)*100
    senior_per = (senior_count/student_count)*100
    python_per = (python_count/student_count)*100
    twenties_per = (twenties_count/student_count)*100
    thirties_per = (thirties_count/student_count)*100
    fourties_per = (fourties_count/student_count)*100
    print("전체 학생수: %s명"%student_count)
    print("* 성별")
    print("- 남: %s명 (%0.1f%%)"% (man_count,man_per))
    print("- 여: %s명 (%0.1f%%)"% (woman_count,woman_per))
    print("전공 여부")
    print("- 전공자(컴퓨터 공학, 통계): %s명 (%s%%)"%(major_count,major_per))
    print("- 프로그래밍 언어 경험자: %s명 (%s%%)"%(language_count,language_per))
    print("- 프로그래밍 언어 상급자: %s명 (%s%%)"%(senior_count,senior_per))
    print("- 파이썬 경험자: %s명 (%s%%)"%(python_count,python_per))
    print("연령대")
    print("- 20대: %s명 (%0.1f%%)%s"%(twenties_count,twenties_per,name2_dict) )
    print("- 30대: %s명 (%0.1f%%)%s"%(thirties_count,thirties_per,name3_dict) )
    print("- 40대: %s명 (%0.1f%%)%s"%(fourties_count,fourties_per,name4_dict) )

def input_information():
    for node in note.getiterator('student'):
        node = Element("name")
        node.text = input("이름을 입력하세요(종료는 'Enter' 입력): ")
        node.append(node)
        ET().write('students_info2.xml')

def search():
    pass

def search_name(name_input):
    count=0
    for child in note.getiterator('student'):
        if name_input in child.get("name"):
            count +=1
    for child in note.getiterator('student'):
        if name_input in child.get("name"):
            if count == 1:
                print("(%s)"%child.get("ID"))
                print("* %s"%child.get("name"))
                print("- 성별: %s"%child.get("sex"))
                print("- 나이: %s"%child.findtext("age"))
                major_tag = child.find("major")
                print("- 전공: %s" % major_tag.text)
                for language_value in child.getiterator("language"):
                  if language_value:
                      for period_value in language_value.getiterator("period"):
                          print("> %s 학습기간:%s,level:%s" % (language_value.get("name"), period_value.get("value"), language_value.get("level")))

                print(" ")
            if count >1:
                print("- %s (%s,%s,%s)"%(child.get("ID"),child.get("name"),child.findtext("age"),child.get("sex")))
def search_age(name_input):


    pass

while True:
    num = input(menu)
    if num == '1':
        summary_information()
    elif num == '2':
        # input_information()
        pass
    elif num == '3':
        second_num = input(second_menu)
        if second_num == '1':
            search_num = input(search_menu)
            if search_num == '1':
                ID_input = input("검색어를 입력하세요: ")
                pass
            if search_num == '2':
                name_input = input("검색어를 입력하세요: ")
                search_name(name_input)
                pass
            if search_num == '3':
                age_input = input("검색어를 입력하세요: ")
                search_age(age_input)
                pass
            if search_num == '4':
                ID_input = input("검색어를 입력하세요: ")
                pass
            if search_num == '5':
                ID_input = input("검색어를 입력하세요: ")
                pass
            if search_num == '6':
                ID_input = input("검색어를 입력하세요: ")
                pass
            if search_num == '7':
                ID_input = input("검색어를 입력하세요: ")
                pass
            if search_num == '8':
                continue
        if second_num == '2':
            full_data()
        if second_num == '3':
            continue

