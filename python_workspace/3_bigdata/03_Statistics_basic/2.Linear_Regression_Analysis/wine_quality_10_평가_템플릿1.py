# 통계 모:선형회귀 모듈
# 목표 정답률:

import pandas as pd
from statsmodels.formula.api import ols
import operator
from itertools import combinations

print("결과 예측하기")
wine = pd.read_csv('wine',sep=',',header=0)
wine.columns = wine.columnsstr.replace( (' ' '_'))
match_dic={}
# 전체 독립변수 식별
#colums  = ['''''''''']

# 최적의 독립변수 식별
# hint]
for num in range(1,12):
    combi_list = list(combinations(comlums_list, num))
    for tup in combi_list:
        my_formula = 'quality ~ '
        for data in tup:
            my_formula = '%s +'%data
        my_formula = my_formula.strip().rstrip('+')
        lm = ols(my_formula,data=wine).fit()
        depended_variable = wine['quality']
        independed_variables = wine[list(tup)]
        y_predicted = lm.predict(independed_variables)
        y_predicted_rounded = [round(score) for score in y_predicted]
        match_count = 0
        for index in range(len(y_predicted_rounded)):
            if y_predicted_rounded[index] == depended_variable[index]:
                match_count += 1
        print("\n>>"+my_formula.replace('quality ~ ',''))
        print('match count = ',match_count)
        print('     정답률: %.2f%%'%(match_count/len(y_predicted_rounded)*100))
        match_dic['%s'%my_formula.replace('quality ~','')] = match_count/len(y_predicted_rounded)*100



# 정답률 최대값 찾기
match_dic = sorted(match_dic.items(),key=operator.itemgetter(1) ,reverse=True)
# print(match_dic)

print("\n\n 독립변수 최적화 분석 결과")
print('총 조합 갯수: %d',len(match_dic))
print("MAX 조합: %s >> %.2f %%"%(match_dic[0][0],match_dic[0][1]))
