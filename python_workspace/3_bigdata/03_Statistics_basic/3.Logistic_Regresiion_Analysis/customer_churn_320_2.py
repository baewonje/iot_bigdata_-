# 목적: 피벗테이블 만들기
import pandas as pd

# def get_stats(group):
#     return {'min' : group.min(), 'max' : group.max(),
#             'count' : group.count(), 'mean' : group.mean(),
#             'std' : group.std()}

# read the data set into a pandas DataFrame
churn = pd.read_csv('churn.csv', sep=',',header=0)

churn.columns = [heading.lower() for heading in
                 churn.columns.str.replace(' ','_').str.replace("\'","").str.strip('?')]

churn['total_charges'] = churn['day_charge'] + churn['eve_charge']+\
                         churn['night_charge'] + churn['intl_charge']

# quit_names = ['1st_quartile', '2nd_quartile', '3rd_quartile', '4th_quartile']
# total_charges_quartiles = pd.qcut(churn.total_charges, 4, labels=quit_names)
# dummies = pd.get_dummies(total_charges_quartiles, prefix='total_charges')
# churn_with_dummies = churn.join(dummies)
print("Debug] churn.pivot_table(['total_charges'], index=['churn','custserv_calls'])")
print(churn.pivot_table(['total_charges'], index=['churn','custserv_calls']))
print("\n\nDebug] churn.pivot_table(['total_charges'], index=['churn'],colomns=['custserv_calls'])")
print(churn.pivot_table(['total_charges'], index=['churn'],columns=['custserv_calls']))
print("""\nDebug] churn.pivot_table(['total_charges'], index=['custserv_calls'], columns=['churn'],
                        aggfunc='mean', fill_value='NaN', margins=True)""")
print(churn.pivot_table(['total_charges'], index=['custserv_calls'], columns=['churn'],
                        aggfunc='mean', fill_value='NaN', margins=True))