# !/usr/bin/env python3
import csv
from datetime import datetime, date
import sys
import MySQLdb
# 아래와 같이 테이블 생성 할 것
# CREATE TABLE IF NOT EXISTS Student_info
#                           (ITT_ID int not null auto_increment primary key,
#                           Student_ID VARCHAR(20),
#                           Name VARCHAR(20),
# 						    Sex VARCHAR(20),
#                           Age int,
#                           Major VARCHAR(20));
main_menu = """
  <메인 메뉴>
1. 생성(Insert)
2. 조회(Select)
3. 변경(Update)
4. 삭제(Delete)
5. 종료
 """

data_menu = """
<2. 데이터 조회>
1. 전체 조회
2. 아이디 조회
3. 이름 조회
4. 성별 조회
5. 나이 조회
6. 전공 조회
7. 이전메뉴
메뉴를 입력하세요: """

con = MySQLdb.connect(host='localhost', port=3306, db='my_student',user='root', passwd='1111',charset='utf8')
c = con.cursor()

def data_insert():
    print("이름, 성별, 나이, 전공순으로 데이터를 입력 하세요.예) 홍길동 남 45 행정학")
    data = input("데이터 입력: ").split()
    c.execute("""INSERT INTO Student_info(Name,Sex,Age,Major) VALUES (%s, %s, %s, %s);""",data)
    con.commit()

def all_select():
    c.execute("SELECT * FROM Student_info")
    rows = c.fetchall()
    for row in rows:
        row_list_output = []
        for column_index in range(len(row)):
            row_list_output.append(str(row[column_index]))
        print(f'{row_list_output}')

def select_main():
    select_ID = input("아이디를 입력하세요: ")
    c.execute(f"SELECT * FROM Student_info WHERE Student_ID = '{select_ID}'")
    rows = c.fetchall()
    for row in rows:
        row_list_output = []
        for column_index in range(len(row)):
            row_list_output.append(str(row[column_index]))
        print(row_list_output)

def select_name():
    select_Name = input("이름를 입력하세요: ")
    c.execute(f"SELECT * FROM Student_info WHERE Name = '{select_Name}'")
    rows = c.fetchall()
    for row in rows:
        row_list_output = []
        for column_index in range(len(row)):
            row_list_output.append(str(row[column_index]))
        print(row_list_output)

def select_Sex():
    select_sex = input("성별을 입력하세요: ")
    c.execute(f"SELECT * FROM Student_info WHERE Sex = '{select_sex}'")
    rows = c.fetchall()
    for row in rows:
        row_list_output = []
        for column_index in range(len(row)):
            row_list_output.append(str(row[column_index]))
        print(row_list_output)

def select_Age():
    select_age = input("나이을 입력하세요: ")
    c.execute(f"SELECT * FROM Student_info WHERE Age = '{select_age}'")
    rows = c.fetchall()
    for row in rows:
        row_list_output = []
        for column_index in range(len(row)):
            row_list_output.append(str(row[column_index]))
        print(row_list_output)

def select_Major():
    select_major = input("나이을 입력하세요: ")
    c.execute(f"SELECT * FROM Student_info WHERE Major = '{select_major}'")
    rows = c.fetchall()
    for row in rows:
        row_list_output = []
        for column_index in range(len(row)):
            row_list_output.append(str(row[column_index]))
        print(row_list_output)

def data_update():
    print("이름, 성별, 나이, 전공, ID 순으로 새로운 데이터를 입력 하세요.")
    update_choice =input("예)홍길동 남 45 행정학 1 : ").split()
    c.execute("UPDATE Student_info SET  Name=%s,Sex=%s, Age=%s,Major=%s WHERE Student_ID=%s;", update_choice)
    print("변경 되었습니다.")
    con.commit()

def delete_main():
    delete_ID = input("아이디를 입력하세요: ")
    output = c.execute(f"SELECT * FROM Student_info WHERE Student_ID = '{delete_ID}' ")
    rows = c.fetchall()
    for row in rows:
        output = []
        for column_index in range(len(row)):
            output.append(str(row[column_index]))
        print(output)
    delete_choice= input("삭제하시겠습니까? (Y/N) : ")
    if delete_choice == 'Y' or 'y':
        c.execute(f"DELETE FROM Student_info WHERE Student_ID = '{delete_ID}' ")
        print("삭제 되었습니다.")
    else:
        pass
    con.commit()

while True:
    main_choice = int(input(main_menu))
    if main_choice == 1:
        data_insert()
    elif main_choice == 2:
        data_choice = int(input(data_menu))
        if data_choice == 1:
            all_select()
        elif data_choice == 2:
            select_main()
        elif data_choice == 3:
            select_name()
        elif data_choice == 4:
            select_Sex()
        elif data_choice == 5:
            select_Age()
        elif data_choice == 6:
            select_Major()
        elif data_choice == 7:
            continue
    elif main_choice == 3:
        data_update()
        pass
    elif main_choice == 4:
        delete_main()
    elif main_choice == 5:
        break

con.commit()
