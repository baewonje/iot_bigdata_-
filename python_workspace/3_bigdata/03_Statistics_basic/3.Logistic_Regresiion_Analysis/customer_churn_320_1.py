# 목적: total_charges를 기준으로 1,2,3,4 분위중 어디에 포함하는지에 대한 정보를
#       2진형 데이터 열로 추가
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

churn['total_charges'] = churn['day_charge'] + churn['eve_charge']+\
                         churn['night_charge'] + churn['intl_charge']

# factor_qcut = pd.qcut(churn.account_length, [0., 0.25, 0.5, 0.75, 1.] )
# grouped = churn.custserv_calls.groupby(factor_qcut)
# print(grouped.apply(get_stats).unstack())

quit_names = ['1st_quartile', '2nd_quartile', '3rd_quartile', '4th_quartile']
total_charges_quartiles = pd.qcut(churn.total_charges, 4, labels=quit_names)
dummies = pd.get_dummies(total_charges_quartiles, prefix='total_charges')
churn_with_dummies = churn.join(dummies)
print(churn_with_dummies.head())
