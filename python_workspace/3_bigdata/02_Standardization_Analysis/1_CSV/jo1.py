#목적 : csv 파일 읽고 쓰기
import sys

# input_file = sys.argv[1] # supplier_data.csv
# output_file = sys.argv[1] # output_files/1output_index_false.csv

category_1 = """
1. 상의
2. 하의
3. 아우터
입력 하세요. : """

category_top = """
1. 티셔츠
2. 셔츠
3. 맨투맨
4. 후드티
5. 블라우스
6. 니트
7. 폴라티
입력 하세요. : """

category_sleeve = """
1. 반팔
2. 긴팔
3. 추가옵션
입력 하세요. : """

category_bottom = """
1. 면바지
2. 청바지
3. 슬랙스
4. 반바지
5. 치마
6. 원피스
입력 하세요. : """

category_outer = """
1. 코트
2. 패딩
3. 자켓
4. 후드집업
5. 바람막이
6. 가디건
7. 야상
입력 하세요. : """

category_color = """
1. 빨강
2. 주황
3. 노랑
4. 초록
5. 파랑
6. 남색
7. 보라
8. 분홍
9. 흰색
10. 검정색
입력 하세요. : """

def top_save(t_shirt_list):
    with open('top_list.csv', 'a', newline= '') as filewriter:
        header = ['sort','sort2','color','option']
        header_list = header
        print(header_list)
        filewriter.write(','.join(map(str,header_list))+'\n')
        filewriter.write(','.join(map(str,t_shirt_list))+'\n')

def short_t_shirt(choice_color):
    global t_shirt_list
    t_shirt_list = []
    sort1 = 't'
    sort2 = 's'
    if choice_color == 1:
        select_color = 'red'
        t_shirt_list.append(sort1)
        t_shirt_list.append(sort2)
        t_shirt_list.append(select_color)
    return t_shirt_list

while True:
    choice_1 = int(input(category_1))
    if choice_1 == 1:
       choice_top = int(input(category_top))
       if choice_top == 1:
           choice_sleeve = int(input(category_sleeve))
           choice_color = int(input(category_color))
           if choice_sleeve == 1:
               short_t_shirt(int(choice_color))
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