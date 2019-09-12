# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 16:40:12 2018

@author: sefira karina

references:
https://www.youtube.com/watch?v=wQ8BIBpya2k&list=PLQVvvaa0QuDfhTox0AjmQ6tvTgMBZBEXN
https://www.bitdegree.org/user/course/python-image-recognition/player/1021
"""
import keras
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers.convolutional import Conv2D, MaxPooling2D
from keras.optimizers import SGD
from keras.constraints import maxnorm

#NOTE : PLEASE LOAD THE DATA THROUGH loading_data.py BEFORE RUNNING THIS FILE

#load the data from the file produced from loading_data.py
def load(self):
    self.X = np.load('saveX.npy')
    self.y = np.load('saveY.npy')
    global X
    def X(): return self.X
    global y
    def y():return self.y
    pass


#make the model
model = Sequential()

model.add(Conv2D(200, (3, 3), input_shape= X.shape[1:], activation='relu', kernel_constraint=maxnorm(3)))
model.add(MaxPooling2D(pool_size=(2, 2)))
#model.add(Dense(64, activation='relu', kernel_constraint=maxnorm(3)))

model.add(Conv2D(200, (3, 3), activation='relu', kernel_constraint=maxnorm(3)))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())
model.add(Dense(64, activation='relu', kernel_constraint=maxnorm(3)))
model.add(Dense(32, activation='softmax'))


model.compile(loss='sparse_categorical_crossentropy', optimizer="adam", metrics=['accuracy'])

#train the model
model.fit(X, y, epochs=29, batch_size=32, validation_split= 0.3)

#save the model into a file to be used later
model.save('trained_model6.h5')

    

