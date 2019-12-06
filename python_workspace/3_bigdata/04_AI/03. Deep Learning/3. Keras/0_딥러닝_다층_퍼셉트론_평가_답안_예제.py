# 데이터 출처: kaggle
# 데이터 개요: 768건의 피마족 당료명 이력데이터
# 데이터 예측 모델: 다중클래스
# 적용 머신러닝 모델: CNN
# 훈련 데이터셋: 5만건
# 검증 데이터셋: 1만건
# 시험 데이터셋: 1만건
# 입력 데이터: 28*28 픽셀데이터
# 은닉층: 6개(Featering Layer: 4개, Fully Connected Layer: 2개)
# 출력 데이터: 10개 Class (0~9까지의 숫자)
# 사용한 활성화 함수
# - Convolution Layer: Relu
# - Output Layer: Softmax
# 사용한 손실함수: categorical_crossentropy
# 사용한 Optimizer: sgd
# Tensorflow 버전: 2.0.0
# 파이썬버전: 3.7.4

# 0. 사용할 패키지 불러오기
import numpy as np
from keras.models import Sequential
from keras.layers import Dense

# 랜덤시드 고정시키기
np.random.seed(5)

# 1. 데이터 준비하기
dataset = np.loadtxt("pima-indians-diabetes.data", delimiter=",")
# 1. Number of times pregnant
# 2. Plasma glucose concentration a 2 hours in an oral glucose tolerance test
# 3. Diastolic blood pressure (mm Hg)
# 4. Triceps skin fold thickness (mm)
# 5. 2-Hour serum insulin (mu U/ml)
# 6. Body mass index (weight in kg/(height in m)^2)
# 7. Diabetes pedigree function
# 8. Age (years)
# 9. Class variable (0 or 1)

# 2. 데이터셋 생성하기
x_train = dataset[:700,0:8]
y_train = dataset[:700,8]
x_test = dataset[700:,0:8]
y_test = dataset[700:,8]

# 3. 모델 구성하기
model = Sequential()
model.add(Dense(12, input_dim=8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# 4. 모델 학습과정 설정하기
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# 5. 모델 학습시키기
model.fit(x_train, y_train, epochs=1500, batch_size=64)

# 6. 모델 평가하기
scores = model.evaluate(x_test, y_test)
print("%s: %.2f%%" %(model.metrics_names[1], scores[1]*100))

# 7. 결과
# accuracy: 80.88%