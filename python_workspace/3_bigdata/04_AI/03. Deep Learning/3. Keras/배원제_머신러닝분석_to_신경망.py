# 데이터 출처: kaggle
# 데이터 개요: 17899개의 pulsar_stars 데이터
# 데이터 예측 모델: 다중클래스
# 적용 머신러닝 모델: 깊은 다층 퍼셉트론 신경망
# 훈련 데이터셋: 13423 건
# 검증 데이터셋: 4475 건
# 시험 데이터셋: 수집데이터로서 시험셋을 확보할 수 없으므로 고려하지 않음
# 입력 데이터: 8개
# 은닉층: 2개
# 출력 데이터: 2개 (1:existent 0:nonexistent)
# 사용한 활성화 함수
# - 제1 은닉층: Relu
# - 제2 은닉층: Relu
# - Output Layer: Sigmoid
# 사용한 손실함수: binary_crossentropy
# 사용한 Optimizer: adam
# Tensorflow 버전: 2.0.0
# 파이썬버전: 3.7.4

import pandas as pd
from datetime import datetime
from sklearn.model_selection import train_test_split
import numpy as np
from keras.models import Sequential
from keras.layers import Dense


match_dic={}

stars = pd.read_csv('pulsar_stars.csv',sep=',',header=0)
stars.columns = stars.columns.str.replace(' ','_')


# 전체 독립변수 식별
# input_data_header=["firstBlood","firstTower","firstInhibitor","firstBaron","firstDragon","firstRiftHerald"]
input_data_header = list(stars.columns.difference(["target_class"]))
input_data_number = len(input_data_header)
label = stars["target_class"]

start_time = datetime.now()

train_data, test_data, train_label, test_label = train_test_split(stars[input_data_header],label)

# 2. 모델 구성하기
model = Sequential()
model.add(Dense(64, input_dim=input_data_number, activation='relu'))
model.add(Dense(64, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# 4. 모델 학습시키기
# hist = model.fit(train_data, test_data, epochs=30, batch_size=32, validation_data=(train_label, test_label))
hist = model.fit(train_data, train_label,epochs=200, batch_size=64)
end_time = datetime.now()

# 5. 학습과정 살펴보기
import matplotlib.pyplot as plt

fig, loss_ax = plt.subplots()

acc_ax = loss_ax.twinx()

loss_ax.set_ylim([0.0, 1.0])
acc_ax.set_ylim([0.0, 1.0])

loss_ax.plot(hist.history['loss'], 'y', label='train loss')
acc_ax.plot(hist.history['accuracy'], 'b', label='train acc')

loss_ax.set_xlabel('epoch')
loss_ax.set_ylabel('loss')
acc_ax.set_ylabel('accuray')

loss_ax.legend(loc='upper left')
acc_ax.legend(loc='lower left')

plt.show()

# 6. 모델 평가하기
scores = model.evaluate(test_data, test_label)
print("%s: %.2f%%"%(model.metrics_names[1],scores[1]*100))

# 결과
# accuracy: 97.47%
