# !/usr/bin/env python
import pandas as pd
import glob
import os
import sys

# supplier_data.csv
# output_files/9output_pandas.csv
input_path = sys.argv[1]
output_file = sys.argv[2]
# pandas에서 분산파일을 읽거나 쓰기 위한 라이브러리는 특별히 제공되지 않는다.
all_files = glob.glob(os.path.join(input_path, 'sales_*'))

all_data_frames = []
for file in all_files:
    data_frame = pd.read_csv(file, index_col=None)
    all_data_frames.append(data_frame)
data_frame_concat = pd.concat(all_data_frames, axis=0, ignore_index = True)

data_frame_concat.to_csv(output_file, index = False)