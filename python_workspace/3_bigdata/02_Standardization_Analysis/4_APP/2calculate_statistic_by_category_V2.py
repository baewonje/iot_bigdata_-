# 목적: 빅데이터에서 카테고리별 통계치 계산하기
import csv
import sys
from datetime import date, datetime

input_file = sys.argv[1] # customer_category_history.csv
output_file = sys.argv[2] # output_files/2output.csv

packages ={}
previous_ID = 'N/A'
previous_widget = 'N/A'
previous_supplier = 'N/A'
previous_cost = 'N/A'
previous_date = 'N/A'
previous_extension = 'N/A'
first_row = True

with open(input_file, 'r', newline='') as input_csv_file:
    filereader = csv.reader(input_csv_file)
    header = (filereader)
    for row in filereader:
        current_ID = row[0]
        current_widget = row[1]
        current_supplier = row[2]
        current_cost = row[3]
        current_date = row[4]
        current_extension = row[5]
        if current_ID not in packages:
            packages[current_ID] = {}
        # if current_widget not in packages[current_ID]:
        #     packages[current_ID][current_widget] = None
        if current_supplier not in packages[current_ID]:
            packages[current_ID][current_supplier] = None
        # if current_cost not in packages[current_ID]:
        #     packages[current_ID][current_cost] = None
        # if current_date not in packages[current_ID]:
        #     packages[current_ID][current_date] = None
        if current_ID != previous_ID:
            if first_row:
                first_row = False
            else:
                if previous_supplier not in packages[previous_ID]:
                    packages[previous_ID][previous_supplier] += str(previous_extension)
                else:
                    packages[previous_ID][previous_supplier] = str(previous_extension)
        else:
            packages[previous_ID][previous_supplier] += str(previous_extension)
        previous_ID = current_ID
        previous_widget = current_widget
        previous_supplier = current_supplier
        previous_cost = current_cost
        previous_date = current_date
        previous_extension = current_extension

header = ['ID_Number', 'widget', 'Supplier','Cost','Date','extension']
with open(output_file, 'w', newline='') as output_csv_file:
    filewriter = csv.writer(output_csv_file)
    filewriter.writerow(header)
    #with 이하 indentation을 맞춰야 한다.
    for customer_ID, customer_ID_value in packages.items():
        # for package_widget, package_widget_value in packages[customer_ID].items():
            for package_supplier, package_supplier_value in packages[customer_ID].items():
                # for package_cost, package_cost_value in packages[customer_ID].items():
                #     for package_date, package_date_value in packages[customer_ID].items():
                        # pass
                row_of_output = []
                print(customer_ID, package_supplier, package_supplier_value)
                row_of_output.append(customer_ID)
                row_of_output.append(package_supplier)
                row_of_output.append(package_supplier_value)

                filewriter.writerow(row_of_output)
