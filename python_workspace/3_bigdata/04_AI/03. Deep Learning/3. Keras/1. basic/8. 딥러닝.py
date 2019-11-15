# 0. 사용할 패키지 불러오기
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras import optimizers
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

# 랜덤시드 고정시키기
np.random.seed(5)

# 1. 데이터 준비하기
dataset = np.loadtxt("pima-indians-diabetes.data", dlimiter=",")

# 2. 데이터셋 생성하기
x_train = dataset[:700, 0:8]
y_train = dataset[:700, 8]
x_test = dataset[700:, 0:8]
y_test = dataset[700:, 8]

# 3. 모델 구성하기
model = Sequential()
model.add(Dense(12, input_dim=8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# 4. 모델 학습과정 설정하기
# 기본 sgd
optimizer_list.
