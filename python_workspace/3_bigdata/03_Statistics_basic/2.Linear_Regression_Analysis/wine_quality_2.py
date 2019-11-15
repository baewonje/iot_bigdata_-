# 목적: 그룹화, 히스토그램

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm

# Read the data set into a pandas DataFrame
wine = pd.read_csv('winequality-both.csv', sep=',', header = 0)
wine.columns = wine.columns.str.replace(' ', '_')

# Display descriptive statistic for quality by wine type
print("< 와인 종류에 따른 기술통제를 출력하기 >")
# 엑셀의 피벗 테이블 효과
print(wine.groupby('type')[['alcohol']].describe().unstack('type'))

# Calculate specific quantities
print("< 특정 사분위 수 계산하기 >")
print(wine.groupby('type')[['quality']].quantile([0.25, 0.75]).unstack('type'))

print("\n"+'='*50)
print("7.2.2 그룹화, 히스토그램, t 검정")

# -----------------------------------------------------------------------------
# ix 함수는 현재 deprecate 되었음.
# 현재 파이썬 버전에서 공식적으로 지원되지 않음
# 다만, 하위 파이썬 호환성을 위해 '수행 시 waring message를 보여주고, 정상 동작' 한다.
# red_wine = wine.ix[wine['type']=='red', 'quality']
# white_wine = wine.ix[wine['type']=='white', 'quality']
# -----------------------------------------------------------------------------
red_wine = wine.loc[wine['type'] == 'red', 'quality']
white_wine = wine.loc[wine['type'] == 'white', 'quality']

sns.set_style("dark")

print(sns.distplot(red_wine, norm_hist=True, kde = False, color="red", label="Red Wine"))
print(sns.distplot(white_wine, norm_hist=True, kde = False, color="blue", label="White Wine"))

# sns.axlabel("Quality Score", "Density")
plt.xlabel("Quality Score")
plt.ylabel("Density")
plt.title("Distribution of Quality by Wine Type")
plt.legend()
plt.show()

# Test whether mean quality is different between red and white wines
print("\n와인의 종류에 따라 품질의 차이를 검정하기")
print(wine.groupby(['type'])[['quality']].agg(['std', 'mean']))
tstat, pvalue, df = sm.stats.ttest_ind(red_wine, white_wine)
print('tstat: %.3f pvalue: %4.f' % (tstat, pvalue))

# pvalue = 유의확률(통계값을 얼마나 신뢰할 수 있는지를 나타내는 지표)
# pvalue가  0.05 보다 작으면 기무가설(=유의가설)을 기각할 수 있다.
# 기무가설 = (두 표본과의 차이가 없다.)
# t 검정(t-test) 서로 다른 두 그룹 간 평균의 차이가 유의미한지를 검정하는 통계적인 방법으로
# 샘플이 등분산성, 독립성을 충족하고 정규성이 부족할 경우 적용할 수 있다.
# 이 예제에서 두 sample 은 독립(independant), 표준편차가 작으므로 등분산성을 충족한다고 볼 수 있다.
# 히스토그램과 개수(30개 이상)로 볼 때 정규분포 데이터를 활용해도 좋다.