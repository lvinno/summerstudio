import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
from matplotlib import image as mpimg
from PIL import Image
import pandas as pd
import numpy as np
import os
import keras
from keras.utils import np_utils
from sklearn.model_selection import train_test_split


def load_data(route):
    path = os.getcwd()+'/'+route+'/' #文件夹目录
    files= os.listdir(path) #得到文件夹下的所有文件名称
    data = []
    for file in files: #遍历文件夹
         if file.find('Store')==-1:
             I = np.array(Image.open(path+file).convert('RGB'))
             data.append(I)
    return data


xianluo_data = load_data('data/n02123045after')
xianluo_label = []
for i in range(len(xianluo_data)):
    xianluo_label.append(0)

yingduan_data = load_data('data/n02123394after')
yingduan_label = []
for i in range(len(yingduan_data)):
    yingduan_label.append(1)

data = xianluo_data + yingduan_data
label = xianluo_label + yingduan_label


# print(data)
X = np.array(data)
y = np.array(label)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=30)

print(X_train.shape[0])
print(y_train)


X_train4D = X_train.reshape(X_train.shape[0],250,250,3).astype('float32')
X_test4D = X_test.reshape(X_test.shape[0],250,250,3).astype('float32')

# normalization
x_train4D_normalized = X_train4D/255
x_test4D_normalized = X_test4D/255

y_trainOne_Hot = np_utils.to_categorical(y_train)
y_testOne_Hot = np_utils.to_categorical(y_test)

from keras.models import Sequential
from keras.layers import Dense,Dropout,Flatten,Conv2D,MaxPooling2D

model = Sequential()

model.add(Conv2D(filters=16,
                 kernel_size=(5,5),
                 padding="same",
                 input_shape=(250,250,3),
                 activation='relu'))


model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Conv2D(filters=36,
                 kernel_size=(5,5),
                 padding="same",
                 activation='relu'))

model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Dropout(0.25))

model.add(Flatten())

model.add(Dense(128,activation="relu"))

model.add(Dense(2,activation="softmax"))


model.compile(loss='categorical_crossentropy',
             optimizer='adam',metrics=['accuracy'])

# train the model
train_history = model.fit(x=x_train4D_normalized,
                          y=y_trainOne_Hot,
                          validation_split=0.2,
                          epochs=10,
                          batch_size=300,
                          verbose=2)


scores = model.evaluate(x_test4D_normalized,y_testOne_Hot)
print('accuracy = ',scores)