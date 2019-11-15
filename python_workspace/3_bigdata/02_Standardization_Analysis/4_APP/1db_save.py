import csv
from datetime import datetime, date
import sys
import MySQLdb

input_file = sys.argv[1]

con = MySQLdb.connect(host='localhost', port=3306, db='suppliers_2012',user='root', passwd='1111',charset='utf8')
c = con.cursor()

file_reader = csv.reader(open(input_file,'r'),delimiter=',')
header = next(file_reader,None)
item_numbers_to_find = []

for row in file_reader:
    data = []
    if row[0] != '':
        for column_index in range(len(header)):
            data.append(str(row[column_index]).strip())
        print(data)
        c.execute("""INSERT INTO Suppliers2(Item_Number, Description, Supplier, Cost, Date) VALUES (%s, %s, %s, %s, %s);""",data)
con.commit()

# Query the sales table
c.execute("SELECT * FROM Suppliers2")
rows = c.fetchall()
for row in rows:
    row_list_output = []
    for column_index in range(len(row)):
        row_list_output.append(str(row[column_index]))
    print(row_list_output)