#목적: 헤더 추가하기

import csv
import sys
input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file, 'r', newline='') as csv_input_file:
    with open(output_file, 'w', newline='') as csv_output_file:
        filereader = csv.reader(csv_input_file)
        filewriter = csv.writer(csv_output_file)
        header_list = ['Supplier Name', 'Invoice Number', 'Part Number', 'Cost', 'Purchase Date']
        filewriter.writerow(header_list)
        for row in filereader:
            filewriter.writerow(row)