# 통계 모델:선형회귀 분석(Linear Regression Analsis)
# 목표 정답률:전체 독립 변수를 종합 한 결과 54.0244%를 초과한 정답률
# 독립 변수 최적화 분석 결과
from _datetime import datetime
import pandas as pd
import operator
from itertools import combinations
from sklearn import metrics, svm

nj = datetime.now()

# <= csv파일 읽고 공백문자를 '_'로 변경하는 전처리 작업
wine = pd.read_csv('winequality-both.csv',sep=',',header=0)
wine.columns = wine.columns.str.replace(' ','_')

match_dic={}

# 전체 독립 변수 식별
colums_list = ['fixed_acidity',	'volatile_acidity',	'citric_acid',	'residual_sugar',
               'chlorides',	'free_sulfur_dioxide',	'total_sulfur_dioxide',
               'density', 'pH',	'sulphates','alcohol']

# <= 최적화된 독립 변수 식별
label = wine['quality']
for num in range(10,12):
    combi_list = list(combinations(colums_list,num))
    for tup in combi_list:
        # 종속 변수 식별
        data_header_list = list(tup)
        clf = svm.SVC(gamma='auto')
        clf.fit(wine[data_header_list], label)
        pre = clf.predict(wine[data_header_list])
        accuracy = metrics.accuracy_score(label,pre)
        # ok_num = 0
        # for index, predict_data in enumerate(pre):
        #    if round(predict_data) == label[index]:
        #        ok_num += 1
        # scores = model_selection.cross_val_score(clf,wine[data_header_list],label, cv=5)
        # accuracy = ok_num / len(label)
        data_header_name = ' '.join(data_header_list)
        match_dic[data_header_name] = accuracy *100
        print(f' 데이터 행 조합: {data_header_name}')
        print(f' 정답률: {accuracy*100} %%')


# 최댓값 찾기
match_dic = sorted(match_dic.items(), key=operator.itemgetter(1),reverse=True)

print("\n\n 독립변수 최적화 분석 결과")
print('총 조합 갯수: %d'%len(match_dic))
print("MAX 조합: %s >> %.2f %%"%(match_dic[0][0],match_dic[0][1]))

ve = datetime.now()
print(ve - nj)