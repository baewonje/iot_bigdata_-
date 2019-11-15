# !/usr/bin/env python3
import sys
import pandas as pd

input_file = sys.argv[1] # sales_2013.xlsx
output_files = sys.argv[2] # output_files/2output_basic.xls

data_frame = pd.read_excel(input_file, 'january_2013', index_col = None)
data_frame_value_matches_pattern = data_frame[data_frame['Customer Name'].str.startswith("J")]

writer = pd.ExcelWriter(output_files)
data_frame_value_matches_pattern.to_excel(writer, sheet_name='jan_13_output', index = False)
writer.save()