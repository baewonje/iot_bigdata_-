# 통계 모:선형회귀 분석(Linear Regression Analysis)
# 목표 정답률:독립변수를 모두 조합 한 결과 53.0244%를 초과한 정답률

import pandas as pd
from statsmodels.formula.api import ols
import operator
from itertools import combinations

print("결과 예측하기")
wine = pd.read_csv('winequality-both.csv',sep=',',header=0)
wine.columns = wine.columns.str.replace(' ','_')

match_dic={}
# 전체 독립변수 식별
colums_list =[]
# 최적의 독립변수 식별
# hint]
# combinations(,)
# lm = ols(, data=).fit()
# y_predicted = lm.predict()


# 정답률 최대값 찾기
match_dic = sorted(, ,)
# print(match_dic)

print("\n\n 독립변수 최적화 분석 결과")
print('총 조합 갯수: %d')
print("MAX 조합: %s >> %.2f %%")
