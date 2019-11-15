# 목적
# 비휘발성인 db에 접속하면 언제나 이전 값을 조회할 수 있다.
import csv
import sqlite3
import sys

con = sqlite3.connect('Suppliers.db')
c = con.cursor()
output = c.execute("SELECT * FROM Suppliers")
rows = output.fetchall()
for row in rows:
    output = []
    for column_index in range(len(row)):
        output.append(str(row[column_index]))
    print(output)