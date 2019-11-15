import json
g_json_big_data = []

with open("ITT_Student1.json", encoding="utf-8") as json_file:
    json_object= json.load(json_file)
    json_string = json.dumps(json_object)
    g_json_big_data = json.loads(json_string)

information_menu = '''
1. 학생 정보 입력
2. 학생 정보 조회
3. 학생 정보 수정
4. 학생 정보 삭제
5. 프로그램 종료
메뉴를 선택하세요: '''

reference_menu = '''
1. 전체 학생 정보 조회
2. ID 검색
3. 이름 검색
4. 나이 검색
5. 주소 검색
6. 과거 수강 횟수 검색
7. 현재 강의를 수강중인 학생
8. 현재 수강 중인 강의명
9. 현재 수강 강사
10. 이전 메뉴
메뉴를 선택하세요: '''

del_menu = '''
1. 전체 삭제
2. 현재 수강 중인 특정 과목정보 삭제
3. 이전 메뉴
메뉴 번호를 선택하세요: '''

def information_inquiry():
    for i in g_json_big_data:
        index= 0
        print("* 학생 ID: %s"% g_json_big_data[index]['student_ID'])
        print("* 이름: %s"% g_json_big_data[index]['student_name'])
        print("* 나이: %s"% g_json_big_data[index]['student_age'])
        print("* 주소: %s"% g_json_big_data[index]['address'])
        print("* 수강 정보")
        print(" + 과거 수강 횟수: %s"% g_json_big_data[index]['total_course_info']['num_of_course_learned'])
        print(" + 과거 수강 과목")
        print("  강의 코드: %s"% g_json_big_data[index]['total_course_info']['learning_course_info'][0]['course_code'])
        print("  강의명: %s"% g_json_big_data[index]['total_course_info']['learning_course_info'][0]['course_name'])
        print("  강사: %s"% g_json_big_data[index]['total_course_info']['learning_course_info'][0]['teacher'])
        print("  개강일: %s"% g_json_big_data[index]['total_course_info']['learning_course_info'][0]['open_date'])
        print("  종료일: %s"% g_json_big_data[index]['total_course_info']['learning_course_info'][0]['close_date'])
        print(" ")
        index +=1

def information_ID():
    search_id = input("검색어를 입력하세요: ")
    index =0
    for i in g_json_big_data:
        if search_id in g_json_big_data[index]['student_ID']:
            print("* 학생 ID: %s" % g_json_big_data[index]['student_ID'])
            print("* 이름: %s" % g_json_big_data[index]['student_name'])
            print("* 나이: %s" % g_json_big_data[index]['student_age'])
            print("* 주소: %s" % g_json_big_data[index]['address'])
            print("* 수강 정보")
            print(" + 과거 수강 횟수: %s" % g_json_big_data[index]['total_course_info']['num_of_course_learned'])
            print(" + 과거 수강 과목")
            print("  강의 코드: %s" % g_json_big_data[index]['total_course_info']['learning_course_info'][0]['course_code'])
            print("  강의명: %s" % g_json_big_data[index]['total_course_info']['learning_course_info'][0]['course_name'])
            print("  강사: %s" % g_json_big_data[index]['total_course_info']['learning_course_info'][0]['teacher'])
            print("  개강일: %s" % g_json_big_data[index]['total_course_info']['learning_course_info'][0]['open_date'])
            print("  종료일: %s" % g_json_big_data[index]['total_course_info']['learning_course_info'][0]['close_date'])
            print(" ")
            index+=1

def student_inquiry(input_inquiry,search_inquiry):
    index = 0
    count = 0
    list = []
    for i in g_json_big_data:
        if input_inquiry in str(g_json_big_data[index][search_inquiry]):
            list.append(index)
            index += 1
            count += 1
        else:
            index += 1
    for index in list:
            if count == 1:
                print("* 학생 ID: %s" % g_json_big_data[index]['student_ID'])
                print("* 이름: %s" % g_json_big_data[index]['student_name'])
                print("* 나이: %s" % g_json_big_data[index]['student_age'])
                print("* 주소: %s" % g_json_big_data[index]['address'])
                print("* 수강 정보")
                print(" + 과거 수강 횟수: %s" % g_json_big_data[index]['total_course_info']['num_of_course_learned'])
                print(" + 과거 수강 과목")
                print("  강의 코드: %s" % g_json_big_data[index]['total_course_info']['learning_course_info'][0][
                    'course_code'])
                print(
                    "  강의명: %s" % g_json_big_data[index]['total_course_info']['learning_course_info'][0]['course_name'])
                print("  강사: %s" % g_json_big_data[index]['total_course_info']['learning_course_info'][0]['teacher'])
                print("  개강일: %s" % g_json_big_data[index]['total_course_info']['learning_course_info'][0]['open_date'])
                print(
                    "  종료일: %s" % g_json_big_data[index]['total_course_info']['learning_course_info'][0]['close_date'])
                print(" ")
            if count > 1:
                print("학생 ID: %s, 학생 이름: %s" % (g_json_big_data[index]['student_ID'], g_json_big_data[index]['student_name']))

def information_learnd(input_inquiry,search_inquiry):
    index = 0
    count = 0
    list = []
    for i in g_json_big_data:
        if input_inquiry in str(g_json_big_data[index]['total_course_info'][search_inquiry]):
            list.append(index)
            index += 1
            count += 1
        else:
            index += 1
    for index in list:
        if count == 1:
            print("* 학생 ID: %s" % g_json_big_data[index]['student_ID'])
            print("* 이름: %s" % g_json_big_data[index]['student_name'])
            print("* 나이: %s" % g_json_big_data[index]['student_age'])
            print("* 주소: %s" % g_json_big_data[index]['address'])
            print("* 수강 정보")
            print(" + 과거 수강 횟수: %s" % g_json_big_data[index]['total_course_info']['num_of_course_learned'])
            print(" + 과거 수강 과목")
            print("  강의 코드: %s" % g_json_big_data[index]['total_course_info']['learning_course_info'][0][
                'course_code'])
            print(
                "  강의명: %s" % g_json_big_data[index]['total_course_info']['learning_course_info'][0]['course_name'])
            print("  강사: %s" % g_json_big_data[index]['total_course_info']['learning_course_info'][0]['teacher'])
            print("  개강일: %s" % g_json_big_data[index]['total_course_info']['learning_course_info'][0]['open_date'])
            print(
                "  종료일: %s" % g_json_big_data[index]['total_course_info']['learning_course_info'][0]['close_date'])
            print(" ")
        if count > 1:
            print("학생 ID: %s, 학생 이름: %s" % (g_json_big_data[index]['student_ID'], g_json_big_data[index]['student_name']))

def information_learning(input_inquiry,search_inquiry):
    index = 0
    count = 0
    list = []
    for i in g_json_big_data:
        if input_inquiry in str(g_json_big_data[index]['total_course_info']['learning_course_info'][0][search_inquiry]):
            list.append(index)
            index += 1
            count += 1
        else:
            index += 1
    for index in list:
        if count == 1:
            print("* 학생 ID: %s" % g_json_big_data[index]['student_ID'])
            print("* 이름: %s" % g_json_big_data[index]['student_name'])
            print("* 나이: %s" % g_json_big_data[index]['student_age'])
            print("* 주소: %s" % g_json_big_data[index]['address'])
            print("* 수강 정보")
            print(" + 과거 수강 횟수: %s" % g_json_big_data[index]['total_course_info']['num_of_course_learned'])
            print(" + 과거 수강 과목")
            print("  강의 코드: %s" % g_json_big_data[index]['total_course_info']['learning_course_info'][0][
                'course_code'])
            print(
                "  강의명: %s" % g_json_big_data[index]['total_course_info']['learning_course_info'][0]['course_name'])
            print("  강사: %s" % g_json_big_data[index]['total_course_info']['learning_course_info'][0]['teacher'])
            print("  개강일: %s" % g_json_big_data[index]['total_course_info']['learning_course_info'][0]['open_date'])
            print(
                "  종료일: %s" % g_json_big_data[index]['total_course_info']['learning_course_info'][0]['close_date'])
            print(" ")
        if count > 1:
            print(
                "학생 ID: %s, 학생 이름: %s" % (g_json_big_data[index]['student_ID'], g_json_big_data[index]['student_name']))

def all_del(all_del):
    list =[]
    index=0
    for i in g_json_big_data:
        if all_del in g_json_big_data[index]['student_ID']:
            list.append(index)
            del g_json_big_data[index]
            with open('ITT_Student1.json', 'w', encoding='utf8') as outfile:
                readable_result = json.dumps(g_json_big_data, indent=4, sort_keys=True, ensure_ascii=False)
                outfile.write(readable_result)
                print('ITT_Student.json SAVED')
            print("완료 ")
        else:
            index+=1
while True:
    choice_menu = input(information_menu)
    if choice_menu =='1':
        pass
    if choice_menu =='2':
        choice_inquiry = input(reference_menu)
        if choice_inquiry == '1':
            information_inquiry()
        if choice_inquiry == '2':
            information_ID()
        if choice_inquiry == '3':
            input_inquiry = input("검색어를 입력하세요: ")
            search_inquiry = 'student_name'
            student_inquiry(input_inquiry,search_inquiry)
        if choice_inquiry == '4':
            input_inquiry =input("검색어를 입력하세요: ")
            search_inquiry = 'student_age'
            student_inquiry(input_inquiry,search_inquiry)
        if choice_inquiry == '5':
            input_inquiry = input("검색어를 입력하세요: ")
            search_inquiry = 'student_address'
            student_inquiry(input_inquiry, search_inquiry)
        if choice_inquiry == '6':
            input_inquiry = input("검색어를 입력하세요: ")
            search_inquiry = 'num_of_course_learned'
            information_learnd(input_inquiry, search_inquiry)
        if choice_inquiry == '7':
            # input_inquiry = input("검색어를 입력하세요: ")
            # search_inquiry = ''
            # information_learning(input_inquiry, search_inquiry)
            pass
        if choice_inquiry == '8':
            input_inquiry = input("검색어를 입력하세요: ")
            search_inquiry = 'course_name'
            information_learning(input_inquiry, search_inquiry)
        if choice_inquiry == '9':
            input_inquiry = input("검색어를 입력하세요: ")
            search_inquiry = 'teacher'
            information_learning(input_inquiry, search_inquiry)
        if choice_inquiry == '10':
            continue
    if choice_menu =='3':
        pass
    if choice_menu =='4':
        del_id = input("삭제할 학생 ID를 입력하세요: ")
        choice_del = input(del_menu)
        if choice_del == '1':
            all_del(del_id)
        if choice_del == '2':
            pass
        if choice_del == '3':
            continue
    if choice_menu =='5':
        break
