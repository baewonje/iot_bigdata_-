import csv
import math

data_type_list = """
    <원하는 서비스를 입력하세요.>
1. 행
2. 열
3. 총합
4. 평균
5. 최대값
6. 최소값
7. 편차
8. 분산
9. 표준편차
10. 정렬(오름차순,내림차순)
11. 종료
: """


def get_row_index(search_key):
    index = 0
    while True:
        if big_data[index][0] == str(search_key):
            break
        else:
            index += 1
    return index;

def print_row(search_key):
    match_row = big_data[get_row_index(search_key)]
    print(" ".join(match_row))

def get_column_instance(column_name):
    col_instance = []
    row_index = big_data[0].index(column_name)
    for row in big_data[1:]:
        col_instance.append(float(row[row_index]))
    return col_instance

def print_column(column_name):
    print(column_name)
    for column_data in get_column_instance(column_name):
        print(column_data)

def my_sum(column_name):
    total_sum = sum(get_column_instance(column_name))
    print("\n""총 합은","%g" % total_sum, "입니다.")

def my_average(column_name):
    column_data_list = get_column_instance(column_name)
    total_sum = sum(column_data_list)
    _average = total_sum/len(column_data_list)
    print("\n""총 합은","%g"%total_sum,"입니다.")
    print("총 갯수는", len(big_data)-1,"개 입니다.")
    print("평균은", "%g" % _average,"입니다.")

def my_max(column_name):
    _max = max(get_column_instance((column_name)))
    print("\n가장 큰 값은","%g"% _max,"입니다.")

def my_min(column_name):
    _min = min(get_column_instance(column_name))
    print("\n가장 작은 값은","%g"% _min,"입니다.")

def my_deviation(column_name):
    column_data_list = get_column_instance(column_name)
    total_sum = sum(column_data_list)
    _average = total_sum / len(column_data_list)
    print('\n'"표본\t평균\t  편차")
    for i in get_column_instance(column_name):
        _deviation = float(i) - float(_average)
        if len("%g" %i) < 3:
            point = ' ' * (3-len("%g"%i))
            print("%g"%i,'\t\t'"%0.1f"%_average,'\t\t'"%0.1f"%_deviation)
def my_standard_deviation(column_name):
    column_data_list = get_column_instance(column_name)
    total_sum = sum(column_data_list)
    _average = sum(column_data_list)
    _variance_sum = 0
    for x in get_column_instance(column_name):
        _variance_sum += (x - _average) ** 2
        _variance = _variance_sum / len(get_column_instance(column_name))
        std = math.sqrt(_variance)
        print('\n'"표준편차값은","%g" % std,"이며,""\n즉, 약","%0.1f" %std,"입니다.")
def my_variance(column_name):
    column_data_list = get_column_instance(column_name)
    total_sum = sum(column_data_list)
    _average = total_sum / len(column_data_list)
    _variance_sum = 0
    for x in get_column_instance(column_name):
        _variance_sum += (x -_average)**2
    _variance = _variance_sum/len(get_column_instance(column_name))
    print('\n'"분산 값은",_variance,"\n즉, 약 ""%0.1f"% _variance,"입니다.")

def my_sorting(column_name):
    column_data_list = get_column_instance(column_name)
    for row_element in column_data_list:
        print("%g"%row_element, end=" ")
    print("\n 오름차순 정렬입니다.")
    ascendant_value_list = sorted(column_data_list, reverse=True)
    as_value = " ".join(str("%g" %i) for i in ascendant_value_list)
    print(as_value)
    print("내림차순 정렬입니다.")
    descendat_value_list = sorted(column_data_list)
    des_value = " ".join(str("%g"%i) for i in descendat_value_list )
    print(des_value)

def check_type(column_name):
    try:
        int_form = ([int(_data) for _data in get_column_instance(column_name)])
        return int_form
    except ValueError:
        float_form = ([float(_data) for _data in get_column_instance(column_name)])
        return float_form

with open('Demographic_Statistics_by_zip_Code.csv', newline='') as infile:
    big_data = list(csv.reader(infile))

while True:
    data_type = int(input(data_type_list))
    if data_type == 1:
        search_key = input("Access Key를 입력하세요: ")
        print_row(search_key)
    elif data_type == 2:
        column_name = input("검색하고자 하는 데이터 필드명을 입력하세요: ")
        print_column(column_name)
    elif data_type == 3:
        column_name = input("총합을 구하고자 하는 데이터 필드명을 입력하세요: ")
        print("시그마(Sigma):∑")
        print_column(column_name)
        my_sum(column_name)
    elif data_type == 4:
        column_name = input("평균을 구하고자 하는 데이터 필드명을 입력하세요: ")
        print_column(column_name)
        my_average(column_name)
    elif data_type == 5:
        column_name = input("최대값을 구하고자 하는 데이터 필드명을 입력하세요: ")
        print_column(column_name)
        my_max(column_name)
    elif data_type == 6:
        column_name = input("최소값을 구하고자 하는 데이터 필드명을 입력하세요: ")
        print_column(column_name)
        my_min(column_name)
    elif data_type == 7:
        column_name = input("편차를 구하고자 하는 데이터 필드명을 입력하세요: ")
        print("표준편차(Standard Deviation) 공식 : ")
        print_column(column_name)
        my_deviation(column_name)
    elif data_type == 8:
        column_name = input("분산을 구하고자 하는 데이터 필드명을 입력하세요: ")
        my_variance(column_name)
    elif data_type == 9:
        column_name = input("표준편차를 하는 데이터 필드명을 입력하세요: ")
        my_sorting(column_name)
    else:
        break


