import csv
import sqlite3
import sys

con = sqlite3.connect('Suppliers.db')
c = con.cursor()
# 전체 레코드 조회 readlines()와 유사
# output = c.execute("SELECT * FROM Suppliers")

# 열 필터링 하는 조건
# SQL문은 대소문자를 구분하지 않는다. 그렇지만 성능을 위해
# SQL문 필드, 테이블명은 일관된 대소 문자 정책을 적용해야 한다.
# output = c.execute("SELECT Supplier_Name FROM Suppliers")
# output = c.execute("SELECT Supplier_Name, Cost FROM Suppliers")
# output = c.execute("SELECT supplier_Name, cost FROM Suppliers")
# output = c.execute("select supplier_Name, cost FROM Suppliers")
# output = c.execute("select supplier_Name, cost FROM Suppliers")

#행 필터링 조건
# output = c.execute("SELECT * FROM suppliers WHERE supplier_name ='Supplier X' ")
# output = c.execute("SELECT * FROM suppliers WHERE part_number > 300 ") # 숙제
# output = c.execute("SELECT * FROM suppliers WHERE part_number < 300 ") # 숙제
output = c.execute("SELECT * FROM suppliers WHERE part_number = 300 ") # 숙제
# output = c.execute("SELECT * FROM suppliers WHERE part_number = 300 or part_number = 7009 ") # 숙제
# output = c.execute("SELECT * FROM suppliers WHERE part_number = 300 and part_number = 7009 ") # 숙제
# output = c.execute("SELECT * FROM suppliers WHERE part_number in('7009','6650')  ") # 숙제
# output = c.execute("SELECT * FROM suppliers WHERE part_number not in('7009','6650')  ") # 숙제
# output = c.execute("select * from Suppliers order by cost")
# output = c.execute("SELECT count(*) from suppliers")

# 행, 열 필터링 하는 조건
# output = c.execute("SELECT supplier_name, cost FROM suppliers WHERE supplier_name='Supplier X' ")
rows = output.fetchall()
print("Select 결과")
for row in rows:
    output = []
    for column_index in range(len(row)):
        output.append(str(row[column_index]))
    print(output)