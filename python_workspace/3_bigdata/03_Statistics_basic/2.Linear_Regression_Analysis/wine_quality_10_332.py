# 통계 모델:선형회귀 분석(Linear Regression Analysis)
# 목표 정답률: 독립 변수를 모두 조합 한 결과 53.0244%를 초과한 정답률

import pandas as pd
from statsmodels.formula.api import ols
import operator
from itertools import combinations

# <= csv파일 읽고 header 라인의 공백문자를 '_'로 변경
wine = pd.read_csv('winequality-both.csv',sep=',',header=0)
wine.columns = wine.columns.str.replace(' ','_')

match_dic={}

# 전체 독립 변수 식별
colums_list = ['fixed_acidity','volatile_acidity','citric_acid',
               'residual_sugar','chlorides','free_sulfur_dioxide',
               'total_sulfur_dioxide','density','pH','sulphates','alcohol']


# 최적 독립 변수 식별
for num in range(1,12):
    combi_list = list(combinations(colums_list,num))
    for tup in combi_list:
        # <= 종속 변수 식별
        my_formula = 'quality ~ '
        for data in tup:
            my_formula+='%s + '%data
        my_formula = my_formula.strip().rstrip('+')
        # 선형 회귀 모델 생성
        lm = ols(my_formula, data=wine).fit()
        dependent_variable = wine['quality']
        independent_variables = wine[list(tup)]
        y_predicted = lm.predict(independent_variables)
        y_predicted_rounded =[round(score) for score in y_predicted]
        match_count = 0
        for index in range(len(y_predicted_rounded)):
           if y_predicted_rounded[index] == dependent_variable.values[index]:
               match_count += 1
        print('\n>> '+my_formula.replace('quality ~ ',''))
        print('>> match count=',match_count)
        print('>> 정답률: %.2f %%'%(match_count/len(y_predicted_rounded)*100))
        match_dic['%s'%my_formula.replace('quality ~ ','')] = match_count/len(y_predicted_rounded)*100


# 정답률 최댓값 찾기
match_dic = sorted(match_dic.items(), key=operator.itemgetter(1),reverse=True)

print("\n\n 독립변수 최적화 분석 결과")
print('총 조합 갯수: %d'%len(match_dic))
print("MAX 조합: %s >> %.2f %%"%(match_dic[0][0],match_dic[0][1]))

#선형회귀 분석
# 독립변수를 종합 한 결과 53.0244%를 초과한 정답률
#csv파일 읽고 공백문자 '_'로 변경
#전체 독립 변수 식별
#최적의 독립변수 식별
#종속 변수 식별
#선형회귀 생성
# 정답률 최댓값 찾기