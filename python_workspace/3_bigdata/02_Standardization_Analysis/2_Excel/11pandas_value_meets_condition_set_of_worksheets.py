# !/usr/bin/env python3
import sys
import pandas as pd

input_file = sys.argv[1] # sales_2013.xlsx
output_files = sys.argv[2] # output_files/2output_basic.xls

my_sheets = [0,1]
threshold = 1900.0

data_frame = pd.read_excel(input_file, sheet_name=my_sheets, index_col=None)

row_list = []
for worksheet_name, data in data_frame.items():
    row_list.append(data[data['Sale Amount'].replace('$', '').replace(',', '').astype(float) > threshold])
filtered_rows = pd.concat(row_list, axis=0, ignore_index=True)

writer = pd.ExcelWriter(output_files)
filtered_rows.to_excel(writer, sheet_name='set_of_worksheets', index=False)
writer.save()