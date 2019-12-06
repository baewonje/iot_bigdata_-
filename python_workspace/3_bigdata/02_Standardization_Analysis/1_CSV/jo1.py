#목적 : csv 파일 읽고 쓰기
import sys
import os
import csv
import pandas as pd
import glob



listnum = 0
id = "ID"
repository_name = 'clothes_repository'
file_name = 'clothes_save_list'
file_format = 'csv'
file_size_limit = 200
dir_delimeter = '/'
is_header = False
is_first = False
initial_file_name = f'{repository_name}{dir_delimeter}{file_name}1.{file_format}'

Crud_Menu="""
1. 옷 저장
2. 옷 조회
3. 옷 수정
4. 옷 삭제
입력하세요: """

Select_Menu="""
1. 전체 조회
2. 상의 조회
3. 하의 조회
5. 아우터 조회
입력 하세요: """

Clothes_Menu="""
1. 상의
2. 하의
3. 아우터
입력하세요: """

Top_Menu="""
1. 티셔츠
2. 셔츠
3. 맨투맨
4. 후드티
5. 블라우스
6. 니트
7. 폴라티
입력하세요: """

Bottom_Menu="""
1. 면바지
2. 청바지
3. 슬랙스
4. 반바지
5. 치마
6. 원피스
입력하세요: """

Outer_Menu="""
1. 코트
2. 패딩
3. 자켓
4. 후드집업
5. 바람막이
6. 가디건
7. 야상
입력하세요: """

Length_Menu="""
1. 반팔
2. 긴팔
3. 추가옵션
입력하세요: """

def color_choice():
    sort_color = int(input(" 1. 빨강\n 2. 주황\n 3. 노랑\n 4. 초록 \n"
                           " 5. 파랑 \n 6. 남색\n 7. 보라\n 8. 블랙\n 9. 흰색\n 입력하세요: "))
    return sort_color
def all_select():
    # supplier_data.csv
    # output_files/9output_pandas.csv
    input_path = sys.argv[1]

    all_files = glob.glob(os.path.join(input_path, 'clothes_save_list*'))

    all_data_frames = []
    for file in all_files:
        data_frame = pd.read_csv(file, index_col=None)
        all_data_frames.append(data_frame)
    data_frame_concat = pd.concat(all_data_frames, axis=0, ignore_index=True)
    print(data_frame_concat)


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
        header_list = ['Number','ID','Sort1','Sort2','Sort3','Color','theme','Memo']
        filewriter.writerow(header_list)
        is_header = False
        is_first = False

    filewriter.writerow(sort_list)

    csv_out_file.close()

def file_count():
    index = len(os.listdir(f'{repository_name}{dir_delimeter}'))
    return index

def sort_classification(sort1,sort2,sort3,sort_color):
    global sort_list,listnum
    listnum += 1

    if sort1 == 1:
        sort1 = "top"
    elif sort1 == 2:
        sort1 = "bottoms"
    elif sort1 == 3:
        sort1 = "outer"

    if sort2 == 1:
        sort2 = "T-shirt"
    elif sort2 == 2:
        sort2 = "shirt"
    elif sort2 == 3:
        sort2 = "man-to-man"
    elif sort2 == 4:
        sort2 = "hoodie"
    elif sort2 == 5:
        sort2 = "blouse"
    elif sort2 == 6:
        sort2 = "knitwear"
    elif sort2 == 7:
        sort2 = "turtleneck"
    elif sort2 == 8:
        sort2 = "cotton"
    elif sort2 == 9:
        sort2 = "jeans"
    elif sort2 == 10:
        sort2 = "slacks"
    elif sort2 == 11:
        sort2 = "breeches"
    elif sort2 == 12:
        sort2 = "skirt"
    elif sort2 == 13:
        sort2 = "dress"
    elif sort2 == 14:
        sort2 = "coat"
    elif sort2 == 15:
        sort2 = "padding"
    elif sort2 == 16:
        sort2 = "jacket"
    elif sort2 == 17:
        sort2 = "hood zip-up"
    elif sort2 == 18:
        sort2 = "Windbreaker"
    elif sort2 == 19:
        sort2 = "cardigan"
    elif sort2 == 20:
        sort2 = "Field jacket"

    if sort3 == 1:
        sort3 = "short"
    elif sort3 == 2:
        sort3 = "long"
    elif sort3 == 2:
        sort3 = "Additional-options"

    if sort_color == 1:
        sort_color = "Red"
    elif sort_color == 2:
        sort_color = "orange"
    elif sort_color == 3:
        sort_color = "yellow"
    elif sort_color == 4:
        sort_color = "green"
    elif sort_color == 5:
        sort_color = "blue"
    elif sort_color == 6:
        sort_color = "navy"
    elif sort_color == 7:
        sort_color = "violet"
    elif sort_color == 8:
        sort_color = "black"
    elif sort_color == 9:
        sort_color = "white"

    sort_list = [listnum,id,sort1,sort2,sort3,sort_color]


while True:
    sort_list =[]
    file_size = 0
    crud = int(input(Crud_Menu))
    if crud == 1:
        sort1 = int(input(Clothes_Menu))
        if sort1 == 1:
            sort2 = int(input(Top_Menu))
            if sort2 == 1:
                sort3 = int(input(Length_Menu))
                sort_classification(sort1,sort2,sort3,color_choice())
                if not os.path.exists(repository_name):
                    os.mkdir(repository_name)
                if not os.path.exists(initial_file_name):
                    is_first = True
                    short_t_shirt(1,sort_list)
                else:
                    short_t_shirt(file_count(),sort_list)
        elif sort1 == 2:
            sort2_1 = int(input(Bottom_Menu))
            sort2_1 += 7
            sort_classification(sort1, sort2_1,0, color_choice())
            if not os.path.exists(repository_name):
                os.mkdir(repository_name)
            if not os.path.exists(initial_file_name):
                is_first = True
                short_t_shirt(1, sort_list)
            else:
                short_t_shirt(file_count(), sort_list)

        elif sort1 == 3:
            sort2_2 = int(input(Outer_Menu))
            sort2_2 += 13
            sort_classification(sort1, sort2_2, 0, color_choice())
            if not os.path.exists(repository_name):
                os.mkdir(repository_name)
            if not os.path.exists(initial_file_name):
                is_first = True
                short_t_shirt(1, sort_list)
            else:
                short_t_shirt(file_count(), sort_list)

        else:
            continue
    elif crud == 2:
        select_Menu = int(input(Select_Menu))
        if(select_Menu == 1):
            all_select()
    elif crud == 3:
        pass
    elif crud == 4:
        pass