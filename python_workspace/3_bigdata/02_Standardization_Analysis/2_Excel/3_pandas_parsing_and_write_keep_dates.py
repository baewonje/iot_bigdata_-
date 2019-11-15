# !/usr/bin/env python3
import pandas as pd
import sys

# sales_2013.xlsx output_files/3output_pandas.xls
input_file = sys.argv[1]
output_file = sys.argv[2]

# date_frame = pd.read_excel(input_file, sheet_name ='january_2013')
# sheetname 은 defrecate 되었음

data_frame = pd.read_excel(input_file, sheet_name='january_2013')

writer = pd.ExcelWriter(output_file)
data_frame.to_excel(writer, sheet_name='jan_13_output', index=False)
writer.save()