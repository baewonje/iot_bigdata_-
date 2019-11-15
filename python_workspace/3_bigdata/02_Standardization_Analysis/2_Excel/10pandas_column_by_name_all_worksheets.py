# !/usr/bin/env python3
import sys
import pandas as pd

input_file = sys.argv[1] # sales_2013.xlsx
output_files = sys.argv[2] # output_files/2output_basic.xls

data_frame = pd.read_excel(input_file, sheet_name=None, index_col=None)

column_output = []
for worksheet_name, data in data_frame.items():
    column_output.append(data.loc[:, ['Customer Name', 'Sale Amount']])
selected_columns = pd.concat(column_output, axis=0, ignore_index=True)

writer = pd.ExcelWriter(output_files)
selected_columns.to_excel(writer, sheet_name='selected_columns_all_worksheets', index=False)
writer.save()