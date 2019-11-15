# 목적: intl_plan과 vmail_plan 열에 대한 이진형 지시변수를 만들고
#       churn 열과 병합하여 새로운 데이터 프레임을 생성하기
import pandas as pd

# def get_stats(group):
#     return {'min' : group.min(), 'max' : group.max(),
#             'count' : group.count(), 'mean' : group.mean(),
#             'std' : group.std()}

# read the data set into a pandas DataFrame
churn = pd.read_csv('churn.csv', sep=',',header=0)

churn.columns = [heading.lower() for heading in
                 churn.columns.str.replace(' ','_').str.replace("\'","").str.strip('?')]

# 예측값을 logit 데이터로 변환하기 위한 전처리 코드
# churn['churn01'] = np.where(churn['churn'] == 'True.', 1., 0.)

# churn['total_charges'] = churn['day_charge'] + churn['eve_charge']+\
#                          churn['night_charge'] + churn['intl_charge']

# factor_qcut = pd.qcut(churn.account_length, [0., 0.25, 0.5, 0.75, 1.] )
# grouped = churn.custserv_calls.groupby(factor_qcut)
# print(grouped.apply(get_stats).unstack())

intl_dummies = pd.get_dummies(churn['intl_plan'], prefix='intl_plan')
vmail_dummies = pd.get_dummies(churn['vmail_plan'],prefix='vmail_plan')
churn_with_dummies = churn[['churn']].join([intl_dummies, vmail_dummies])
print(churn_with_dummies.head())
