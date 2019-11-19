import numpy as np

from keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt

# 랜덤시드 고정시키기
np.random.seed(3)

from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense, Activation,Flatten
from keras.layers.convolutional import Conv2D, MaxPooling2D
import matplotlib.pyplot as plt

# 1. 데이터 셋 불러오기
# ImageDataGenerator: 케라스에서 이미지 전처리를 용이하게 해주는 클래스
train_datagen = ImageDataGenerator(rescale=1./255)

train_denerator = train_datagen.flow_from_directory('handwriting_shape/train', target_size=(24, 24),
                                                    batch_size=3, class_mode='categorical')
test_datagen = ImageDataGenerator(rescale=1./255)
test_generator = test_datagen.flow_from_directory('hard_handwriting_shape/test', target_size=(24, 24),
                                                    batch_size=3, class_mode='categorical')


# 2. 모델 구성하기
model = Sequential()
model.add(Conv2D(32, kernel_size=(3,3), activation='relu', input_shape=(24, 24, 3)))
model.add(Conv2D(64,(3,3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
#  이미지를 일차원으로 바꿔주는 Flatten 레이어
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dense(3, activation='softmax'))

# 3. 모델 학습과정 설정하기
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# 4. 모델 학습시키기
model.fit_generator(train_denerator,steps_per_epoch=15, epochs=200, validation_data=test_generator,
                    validation_steps=5)

# 6. 모델 평가하기
print("--Evaluate --")
scores = model.evaluate_generator(test_generator,steps=5)
print("%s: %.2f%%" %(model.metrics_names[1], scores[1]*100))

# 7. 모델 사용하기
print("-- Evaluate --")
scores = model.evaluate_generator(test_generator, steps=5)
print("%s: %.2f%%" %(model.metrics_names[1], scores[1]*100))

# 6. 모델 예측하기
print("-- Predict --")
output = model.predict_generator(test_generator, steps=5)
np.set_printoptions(formatter={'float': lambda x: "{0:0.3f}".format(x)})
print(test_generator.class_indices)
print(output)

# 결과
# Accuracy : 33.33%
