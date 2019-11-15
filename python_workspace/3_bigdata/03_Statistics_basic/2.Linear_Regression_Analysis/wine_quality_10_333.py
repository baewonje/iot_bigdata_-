# 통계 모델:선형 회귀 분석
# 목표 정답률:독립변수를 모두 조합 한 결과 53.0244% 를 초과한 정답률

import pandas as pd
from statsmodels.formula.api import ols
import operator
from itertools import combinations

# <= scv 파일을 읽고 공백문자를 '_'로 변경
wine = pd.read_csv('winequality-both.csv',sep=',',header=0)
wine.columns = wine.columns.str.replace(' ','_')

match_dic={}

# 전체 독립 변수 식별
colums_list = []

# 최적의 독립 변수 식별
for num in range(1,12):
    combi_list = list(combinations(,))
    for tup in combi_list:

        # <= 종속 변수 식별
        my_formula = 'quality ~ '
        for data in tup:
            my_formula+='%s + '%data
        my_formula = my_formula.strip().rstrip('+')

        # <= 선형회귀 생성
        lm = ols(my_formula, data=wine).fit()

#        dependent_variable =
#        independent_variables =
#        y_predicted = lm.predict()
#        y_predicted_rounded =
#
#        for index in range()):
#            if :
#                pass
#        print('\n>> '+my_formula.replace('quality ~ ',''))
#        print('>> match count=',)
#        print('>> 정답률: %.2f %%'%())
#        match_dic[] =


# 정답률 최댓값 찾기
match_dic = sorted(, key=operator.itemgetter(),)

print("\n\n 독립변수 최적화 분석 결과")
print('총 조합 갯수: %d'%len())
print("MAX 조합: %s >> %.2f %%"%(match_dic[][],match_dic[][]))
