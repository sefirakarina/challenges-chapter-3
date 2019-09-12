# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 18:09:35 2018

@author: Sefira Karina

references:
https://www.youtube.com/watch?v=wQ8BIBpya2k&list=PLQVvvaa0QuDfhTox0AjmQ6tvTgMBZBEXN
"""
#NOTE : Please make sure you have the trained_model6.h5 in the same folder as this file
#       if you don't have the trained model yet, download it in https://mega.nz/#!zygnUSra!Fvw1sFiO9PKnWZ7Ya-sgzDqCIjZZSfGyCUg2pb4041o
#       if you want to make your own model, run loading_data.py to load data, then run train_data.py to get the training file

import numpy as np
import matplotlib.pyplot as plt
import os
import cv2
import random
from PIL import Image
from keras.models import load_model

#directory = r"F:\[SEMESTER 5]\Intelligent Systems\fp\fpp\image" #directory of the datasets
directory = r"C:\Users\Sefira Karina\OneDrive\5th semester\Intelligence Systems\intelligence-systems\image\[TEST]" #directory of the datasets
categories = ['no_traffic', 'traffic'] #image categories

test_data = []

def create_test_data():
    temp = 0
    for category in categories:
        path = os.path.join(directory,category)  #file path for every category folder
        class_num = categories.index(category)  #to put which image in which category
        if temp == 0: #store no_traffic images name
            global files
            files = os.listdir(path)
            temp = temp +1
        if temp==1:#store traffic images name
            global files2
            files2 = os.listdir(path)
        for image in os.listdir(path):
            #change the image into an array, change the colors into grayscale
            imgs = cv2.imread(os.path.join(path,image), cv2.IMREAD_GRAYSCALE)
            img_resize = cv2.resize(imgs, (200, 200))
            test_data.append([img_resize, class_num])
            
create_test_data()


#put them into variables to be used in the neural network
X = [] #features (the image's features)
y = [] #labels (where the image is categorized in)

for features, label in test_data:
    X.append(features)
    y.append(label)
    
#convert X to numpy array and reshape the data according to image size and color scale
X = np.array(X).reshape(-1, 200, 200, 1)

X = X/255.0

#load the model from the file produced by train_data.py
model = load_model('trained_model6.h5')

#predict the data
prediction = model.predict_classes(X)

#list all image file name from traffic and no_traffic
all_files = files + files2

#print file name, the true category, and the prediction category
for i in range(0,len(y)):
    print("Prediction ", i+1)
    print("file name           : ", all_files[i])
    print("true category       : ", categories[y[i]] )
    print("prediction category : ", categories[prediction[i]] )
    print("---------------------------------------")

correct = 0
incorrect = 0

#calculate the accuracy of the test
for i in range(0, len(prediction)):
    if y[i] == prediction[i]:
        correct += 1
    else:
        incorrect +=1
print("number of testing images = " , len(prediction)) 
print("correct prediction = " , correct)  
print("testing accuracy = ", correct/len(prediction) *100 ,"%")

