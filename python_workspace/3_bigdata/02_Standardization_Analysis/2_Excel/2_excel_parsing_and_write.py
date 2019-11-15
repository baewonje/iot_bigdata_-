# xrld 모듈설치
# 목적: 엑셀 기본 정보 확인
import sys
from xlrd import open_workbook
from xlwt import Workbook

input_file = sys.argv[1] # sales_2013.xlsx
output_files = sys.argv[2] # output_files/2output_basic.xls

output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet('jan_2013_output')

# 단일 worksheet  처리하기
with open_workbook(input_file) as workbook:
    worksheet = workbook.sheet_by_name('january_2013')
    for row_index in range(worksheet.nrows):
        for column_index in range(worksheet.ncols):
            output_worksheet.write(row_index, column_index, worksheet.cell_value(row_index, column_index))
output_workbook.save(output_files)
