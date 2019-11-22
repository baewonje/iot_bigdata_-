# 데이터 출처: kaggle
# 데이터 개요: 511, 유리를 위한 다양한 속성(화학원소)들로부터 type 구별
# 데이터 예측 모델: 이진클래스
# 적용 머신러닝 모델: 깊은 다층 퍼셉트론 신경망
# 훈련 데이터셋:  160건
# 검증 데이터셋:  건
# 시험 데이터셋: 수집데이터로서 시험셋을 확보할 수 없으므로 고려하지 않음
# 입력 데이터:  10개 항목의 데이터
# 은닉층: 2개
# 사용한 활성화 함수
# - 제1 은닉층: Relu
# - 제2 은닉층: Relu
# - Output Layer: Softmax
# 사용한 손실함수: categorical_crossentropy
# 사용한 Optimizer: rmsprop
# Tensorflow 버전: 2.0.0
# 파이썬버전: 3.7.4

import pandas as pd
from datetime import datetime
from sklearn.model_selection import train_test_split
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import to_categorical

np.random.seed(5)
match_dic={}

zoo_class = pd.read_csv('zoo.csv',sep=',',header=0)
zoo_class.columns = zoo_class.columns.str.replace(' ','_')


# 전체 독립변수 식별
input_data_header = list(zoo_class.columns.difference(["animal_name","class_type"]))
input_data_number = len(input_data_header)
label = zoo_class["class_type"]

start_time = datetime.now()

train_data, test_data, train_label, test_label = train_test_split(zoo_class[input_data_header],label)
train_label = to_categorical(train_label, num_classes=7)
test_label = to_categorical(test_label, num_classes=7)

# 훈련셋과 시험셋 불러오기
# x_train = x_train.reshape(60000, width * height).astype('float32') / 255.0
# x_test = x_test.reshape(10000, width * height).astype('float32') / 255.0

# 모델 구성하기
model = Sequential()
model.add(Dense(64, input_dim=input_data_number, activation='relu'))
model.add(Dense(64, activation='relu'))
# model.add(Dense(6, activation='sigmoid'))
model.add(Dense(7, activation='softmax'))

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
# model.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['accuracy'])

# 4. 모델 학습시키기
hist = model.fit(train_data, train_label, epochs=20000, batch_size=64, validation_data=(test_data, test_label))
# hist = model.fit(train_data, train_label, epochs=1000, batch_size=64)

end_time = datetime.now()

# 5. 학습과정 살펴보기
import matplotlib.pyplot as plt

fig, loss_ax = plt.subplots()

acc_ax = loss_ax.twinx()

loss_ax.plot(hist.history['loss'], 'y', label='train loss')
loss_ax.plot(hist.history['val_loss'], 'r', label='val loss')

# acc_ax.plot(hist.history['acc'], 'b', label='train acc')
acc_ax.plot(hist.history['accuracy'], 'b', label='train acc')
# acc_ax.plot(hist.history['val_acc'], 'g', label='val acc')
acc_ax.plot(hist.history['val_accuracy'],'g', label='val acc')

loss_ax.set_xlabel('epoch')
loss_ax.set_ylabel('loss')
acc_ax.set_ylabel('accuray')

loss_ax.legend(loc='upper left')
acc_ax.legend(loc='lower left')

plt.show()

# 6. 모델 평가하기
loss_and_metrics = model.evaluate(test_data, test_label, batch_size=32)
print('loss_and_metrics : ' + str(loss_and_metrics))

scores = model.evaluate(test_data, test_label)
print("%s: %.2f%%"%(model.metrics_names[1],scores[1]*100))