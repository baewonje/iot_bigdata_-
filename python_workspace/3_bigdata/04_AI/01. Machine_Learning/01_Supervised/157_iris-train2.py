from sklearn import svm,metrics
import pandas as pd
import random, re
from sklearn.model_selection import  train_test_split

# 붗꽃의 CSV 데이터 읽어 들이기 ---(*1)
csv = pd.read_csv('iris.csv')
# 필요한 열 추출하기 ---(*2)
# csv_data = csv[["SepalLength","SepalWidth","PetalLength","PetalWidth"]]
csv_data = csv[["SepalLength","SepalWidth","PetalLength","PetalWidth"]]
csv_label = csv["Name"]
# 학습 전용 데이터와 테스트 전용 데이터로 나누기 ---(*33_bigdata/04_AI/01. Machine_Learning/157_iris-train2.py:13

ac_score = metrics.accuracy_score(test_label,pre)
print("전체 데이터 수: %d"%len(csv_data))
print("학습 전용 데이터 수: %d"%len(train_data))
print("테스트 데이터 수: %d"%len(test_data))
print("정답률 =",ac_score)

