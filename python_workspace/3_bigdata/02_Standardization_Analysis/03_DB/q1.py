# !/usr/bin/env python3
import csv
from datetime import datetime, date
import sys
import MySQLdb
# 아래와 같이 테이블 생성 할 것
# CREATE TABLE IF NOT EXISTS Suppliers2
                          # (ITT_ID int not null auto_increment primary key,
                          # Supplier_Name VARCHAR(20),
                          # Invoice_Number VARCHAR(20),
						    # Part_Number VARCHAR(20),
                          # Cost FLOAT,
                          # Purchase_Date DATE);

# path to and name of a CSV input file
input_file = sys.argv[1] #supplier_data.csv

# db=Database명  create database my_suppliers <= 이렇게 생성한 db명과 매칭
con = MySQLdb.connect(host='localhost', port=3306, db='my_student',user='root', passwd='1111', charset='utf8')
c = con.cursor()

# Read the CSV file
# Insert the data into the Suppliers table
file_reader = csv.reader(open(input_file,'r'),delimiter=',')
header = next(file_reader,None)
for row in file_reader:
    data = []
    for column_index in range(len(header)):
            data.append(str(row[column_index]).strip())
    print(data)
    c.execute("""INSERT INTO Student_info(Student_ID, Name, Sex, Age, Major) VALUES (%s, %s, %s, %s, %s);""",data)
con.commit()

# Query the sales table
c.execute("SELECT * FROM Student_info")
rows = c.fetchall()
for row in rows:
    row_list_output = []
    for column_index in range(len(row)):
        row_list_output.append(str(row[column_index]))
    print(row_list_output)