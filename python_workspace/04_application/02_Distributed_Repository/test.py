# 분산 저장 v6
# 헤더파일 중복저장 되는 문제 해결
import os
import csv
import glob
from datetime import date
from xlrd import open_workbook, xldate_as_datetime
from xlwt import Workbook

message = """
1. 환경설정
2. 작업수행
3. 종료
입력하세요: """

type_message = """
1.Type A 데이터 수집
2.Type B 데이터 수집
3.이전 메뉴
"""
output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet('시뮬레이션_서울특별시_관광지별_방문객')
base_repository_name = 'Bigdata_repository'
Type_A_repository = 'Type_A'
Type_B_repository = 'Type_B'
dir_delimeter = '/'
file_name= '시뮬레이션_서울특별시_관광지별_방문객'
file_format_A = 'csv'
file_format_B = 'xls'
initial_file_name_A =f'{base_repository_name}{dir_delimeter}{Type_A_repository}{dir_delimeter}{file_name}1.{file_format_A}'
initial_file_name_B =f'{base_repository_name}{dir_delimeter}{Type_B_repository}{dir_delimeter}{file_name}1.{file_format_B}'
simulation_count = 100
simulation_data = ['1111','종로구','서울특별시','경복궁','1','14123','43435']
file_size_limit_A = 10000
file_size_limit_B = 10000
is_header = False
is_first = False

def get_request_url():
    pass

def getTourPointVisitor():
    pass

def getTourPointData_A(filewriter):
    filewriter.writerow(simulation_data)
    return

def get_dest_file_name_A(file_index):
    global is_header
    dest_file_name =f'{base_repository_name}{dir_delimeter}{second_repository_name}{dir_delimeter}{file_name}{str(file_index)}.{file_format_A}'

    try:
        file_size = os.path.getsize(dest_file_name)
        print(f"' {dest_file_name}' file size : {file_size}")
        print(f"파일당 size 제한: {file_size_limit_A}")

        if file_size > file_size_limit_A:
            dest_file_name =f'{base_repository_name}{dir_delimeter}{second_repository_name}{dir_delimeter}{file_name}{str(file_index+1)}.{file_format_A}'
            is_header = True
        else:
            is_header = False
    except:
        pass

    return dest_file_name

def save_file_A(index):
    dest_file_name = get_dest_file_name_A(index)

    csv_out_file = open(dest_file_name, 'a', newline='')
    filewriter = csv.writer(csv_out_file)

    if is_header == True or is_first == True:
        header_list = ['addrCd', 'gungu', 'sido', 'resNm', 'rnum', 'csForCnt', 'csNatCnt']
        filewriter.writerow(header_list)

    for index in range(simulation_count):
        getTourPointData_A(filewriter)

    csv_out_file.close()

def file_count_A():
    index = len(os.listdir(f'{base_repository_name}{dir_delimeter}{second_repository_name}'))
    return index


def save_file_B(file_index):
    global is_header
    dest_file_name = f'{base_repository_name}{dir_delimeter}{second_repository_name}{dir_delimeter}{file_name}{str(file_index)}.{file_format_B}'

    try:
        file_size = os.path.getsize(dest_file_name)
        print(f"' {dest_file_name}' file size : {file_size}")
        print(f"파일당 size 제한: {file_size_limit_B}")

        if file_size > file_size_limit_B:
            dest_file_name = f'{base_repository_name}{dir_delimeter}{second_repository_name}{dir_delimeter}{file_name}{str(file_index + 1)}.{file_format_B}'
            is_header = True
        else:
            is_header = False
    except:
        pass

    all_data = []
    sub_list = []
    if is_header == True or is_first == True:
        header_list = ['addrCd', 'gungu', 'sido', 'resNm', 'rnum', 'csForCnt', 'csNatCnt']
        all_data.append(header_list)
    for index in range(simulation_count):
        sub_list.append(simulation_data)
    all_data.extend(sub_list)
    for list_index, output_list in enumerate(all_data):
        for element_index, element in enumerate(output_list):
            # output_worksheet = dest_file_name.add_sheet("Sheet 1", cell_overwrite_ok=True)
            output_worksheet.write(list_index, element_index, element)

    output_workbook.save(dest_file_name)

def file_count_B():
    index = len(os.listdir(f'{base_repository_name}{dir_delimeter}{second_repository_name}'))
    return index



print("경량화 빅데이터 저장소 시뮬레이션 v12.4.1 - 배원제.")
input("<= 엔터키를 눌러 시작하세요.")
while True:
    file_size = 0
    choice = int(input(message))
    if choice == 1:
        print('\n\t\t < 환경설정메뉴 >')
        print(f" 1. Base Repository 명:{base_repository_name}")
        print(f" 2. Type A Repository 명: {Type_A_repository}")
        print(f" 3. Type A 포멧 : {file_format_A}")
        print(f" 4. Type A 데이터용량제한:{file_size_limit_A}")
        print(f" 5. Type B Repository 명:{Type_B_repository}")
        print(f" 6. Type B 포멧: {file_format_B}")
        print(f" 7. Type B 데이터용량제한: {file_size_limit_B}")
        print("  8. 이전메뉴")
        change_choice = int(input("메뉴를 입력하세요: "))
        if change_choice == 1:
            base_repository_name = input("새로운 base repository 명을 입력하세요: ")
        elif change_choice == 2:
            Type_A_repository = input("새로운 폴더 명을 입력하세요: ")
        elif change_choice == 3:
            file_format_A = input("새로운 파일 포맷명을 입력하세요: ")
        elif change_choice == 4:
            file_size_limit_A = input("새로운 데이터 용량 제한값을 입력하세요: ")
        elif change_choice == 5:
            Type_B_repository = input("새로운 폴더 명을 입력하세요: ")
        elif change_choice == 6:
            file_format_B = input("새로운 파일 포맷명을 입력하세요: ")
        elif change_choice == 7:
            file_size_limit_B = input("새로운 데이터 용량 제한값을 입력하세요: ")
        elif change_choice == 8:
            continue

    elif choice == 2:
        type_choice = int(input(type_message))
        if type_choice == 1:
            second_repository_name = Type_A_repository
            if not os.path.exists(base_repository_name):
                os.mkdir(base_repository_name)
            if not os.path.exists(f'{base_repository_name}/{Type_A_repository}'):
                os.mkdir(f'{base_repository_name}/{Type_A_repository}')
            if not os.path.exists(initial_file_name_A):
                is_first = True
                save_file_A(1)
            else:
                save_file_A(file_count_A())
        elif type_choice == 2:
            second_repository_name = Type_B_repository
            if not os.path.exists(base_repository_name):
                os.mkdir(base_repository_name)
            if not os.path.exists(f'{base_repository_name}/{Type_B_repository}'):
                os.mkdir(f'{base_repository_name}/{Type_B_repository}')
            if not os.path.exists(initial_file_name_B):
                is_first = True
                save_file_B(1)
            else:
                save_file_B(file_count_B())
        elif type_choice == 3:

            continue
        print("메인 기능 수행")

    elif choice == 3:
        break
0