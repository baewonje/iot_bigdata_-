#목적 : csv 파일 읽고 쓰기
import sys
import os
import csv

file_name = 'clothes_save_list'
file_format = 'csv'
file_size_limit = 10000
is_header = False
is_first = False


def get_dest_file_name(file_index):
    global is_header
    header = ['sort1', 'sort2', 'sort3', 'color', 'option']
    dest_file_name = f'{file_name}{str(file_index)}.{file_format}'
    try:
        file_size = os.path.getsize(dest_file_name)

        if file_size > file_size_limit:
            dest_file_name = f'{file_name}{str(file_index+1)}.{file_format}'
            is_header = True
        else:
            is_header = False
    except:
        pass

    return dest_file_name

def short_t_shirt(index,choice_color):
    dest_file_name = get_dest_file_name(index)

    csv_out_file = open(dest_file_name,'a',newline='')
    filewriter = csv.writer(csv_out_file)

    if is_header == True or is_first == True:
        header_list = ['sort1','sort2','sort3','color','memo']
        filewriter.writerow(header_list)



def file_count():
    index = len(os.listdir(f'{file_name}'))
    return index

while True:
    sort1 = int(input(" 1. 상의\n 2. 하의\n 3. 아우터\n 입력하세요: "))
    sort2 = int(input(" 1. 티셔츠\n 2. 셔츠\n 3. 맨투맨 \n 4. 후드티 \n"
                      " 5. 블라우스\n 6. 니트\n 7. 폴라티\n 입력하세요: "))
    sort3 = int(input(" 1. 반팔\n 2. 긴팔 \n 3. 추가옵션\n 입력하세요: "))
    sort2_1 = int(input(" 1. 면바지 \n 2. 청바지 \n3. 슬랙스 \n 4. 반바지 "
                        "\n5. 치마\n 6. 원피스\n 입력하세요: "))
    sort_color = int(input(" 1. 빨강\n 2. 주황\n 3. 노랑\n 4. 초록 \n"
                           " 5. 파랑 \n 6. 남색\n 7. 보라\n 8. 블랙\n 9. 흰색\n 입력하세요: "))
    if choice_1 == 1:
       choice_top = int(input(category_top))
       if choice_top == 1:
           choice_sleeve = int(input(category_sleeve))
           choice_color = int(input(category_color))
           if choice_sleeve == 1:
               file_count()
               short_t_shirt(file_count(),int(choice_color))
               top_save(t_shirt_list)
           elif choice_sleeve == 2:
               pass
           elif choice_sleeve == 3:
               pass
           else:
               continue
       elif choice_top == 2:
           if choice_sleeve == 1:
               pass
           elif choice_sleeve == 2:
               pass
           elif choice_sleeve == 3:
               pass
           else:
               continue
       elif choice_top == 3:
           if choice_sleeve == 1:
               pass
           elif choice_sleeve == 2:
               pass
           elif choice_sleeve == 3:
               pass
           else:
               continue
       elif choice_top == 4:
           if choice_sleeve == 1:
               pass
           elif choice_sleeve == 2:
               pass
           elif choice_sleeve == 3:
               pass
           else:
               continue
       elif choice_top == 5:
           if choice_sleeve == 1:
               pass
           elif choice_sleeve == 2:
               pass
           elif choice_sleeve == 3:
               pass
           else:
               continue
       elif choice_top == 6:
           if choice_sleeve == 1:
               pass
           elif choice_sleeve == 2:
               pass
           elif choice_sleeve == 3:
               pass
           else:
               continue
       elif choice_top == 7:
           if choice_sleeve == 1:
               pass
           elif choice_sleeve == 2:
               pass
           elif choice_sleeve == 3:
               pass
           else:
               continue
       else:
           continue
    elif choice_1 == 2:
      pass
    elif choice_1 == 3:
       pass
    else:
        continue