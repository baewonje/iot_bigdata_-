#목적 : csv 파일 읽고 쓰기
import sys
import os
import csv

repository_name = 'clothes_repository'
file_name = 'clothes_save_list'
file_format = 'csv'
file_size_limit = 200
dir_delimeter = '/'
is_header = False
is_first = False
initial_file_name = f'{repository_name}{dir_delimeter}{file_name}1.{file_format}'


def get_dest_file_name(file_index):
    global is_header
    header = ['sort1', 'sort2', 'sort3', 'color', 'option']
    dest_file_name = f'{repository_name}{dir_delimeter}{file_name}{str(file_index)}.{file_format}'
    try:
        file_size = os.path.getsize(dest_file_name)
        print(f"' {dest_file_name}' file size : {file_size}")
        print(f"파일당 size 제한: {file_size_limit}")

        if file_size > file_size_limit:
            dest_file_name = f'{repository_name}{dir_delimeter}{file_name}{str(file_index+1)}.{file_format}'
            is_header = True
        else:
            is_header = False
    except:
        pass

    return dest_file_name

def short_t_shirt(index,sort_list):
    global  is_header,is_first

    dest_file_name = get_dest_file_name(index)

    csv_out_file = open(dest_file_name,'a',newline='')
    filewriter = csv.writer(csv_out_file)

    if is_header == True or is_first == True:
        header_list = ['sort1','sort2','sort3','color','memo']
        filewriter.writerow(header_list)
        is_header = False
        is_first = False

    filewriter.writerow(sort_list)

    csv_out_file.close()

def file_count():
    index = len(os.listdir(f'{repository_name}{dir_delimeter}'))
    return index

def sort_classification(sort1,sort2,sort3,sort_color):
    global sort_list

    if sort1 == 1:
        sort1 = "Top"
    elif sort1 == 2:
        sort1 = "Bottoms"
    elif Sort1 == 3:
        sort1 = "Outer"
    if sort2 == 1:
        sort2 = "T-shirt"
    if sort3 == 1:
        sort3 = "short"
    if sort_color == 1:
        sort_color = "Red"
    sort_list = [sort1,sort2,sort3,sort_color]


while True:
    sort_list =[]
    file_size = 0
    sort1 = int(input(" 1. 상의\n 2. 하의\n 3. 아우터\n 입력하세요: "))

    if sort1 == 1:
        sort2 = int(input(" 1. 티셔츠\n 2. 셔츠\n 3. 맨투맨 \n 4. 후드티 \n"
                          " 5. 블라우스\n 6. 니트\n 7. 폴라티\n 입력하세요: "))
        if sort2 == 1:
            sort3 = int(input(" 1. 반팔\n 2. 긴팔 \n 3. 추가옵션\n 입력하세요: "))
            sort_color = int(input(" 1. 빨강\n 2. 주황\n 3. 노랑\n 4. 초록 \n"
                                   " 5. 파랑 \n 6. 남색\n 7. 보라\n 8. 블랙\n 9. 흰색\n 입력하세요: "))
            print(sort1,sort2,sort3,sort_color)
            sort_classification(sort1,sort2,sort3,sort_color)
            if not os.path.exists(repository_name):
                os.mkdir(repository_name)
            if not os.path.exists(initial_file_name):
                is_first = True
                short_t_shirt(1)
            else:
                short_t_shirt(file_count(),sort_list)
    elif sort1 == 2:
        sort2_1 = int(input(" 1. 면바지 \n 2. 청바지 \n3. 슬랙스 \n 4. 반바지 "
                            "\n5. 치마\n 6. 원피스\n 입력하세요: "))

    elif sort1 == 3:
        pass
    else:
        continue