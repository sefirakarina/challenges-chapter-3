# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 12:54:12 2018
@author: ri

references:
https://www.youtube.com/watch?v=wQ8BIBpya2k&list=PLQVvvaa0QuDfhTox0AjmQ6tvTgMBZBEXN
https://www.bitdegree.org/user/course/python-image-recognition/player/1021
http://makeyourownneuralnetwork.blogspot.com/2018/02/saving-and-loading-neural-networks.html
"""

import numpy as np
import matplotlib.pyplot as plt
import os
import cv2
import random
from PIL import Image

#directory = r"F:\[SEMESTER 5]\Intelligent Systems\fp\fpp\image"
directory = r"C:\Users\Sefira Karina\OneDrive\5th semester\Intelligence Systems\intelligence-systems\image" #directory of the datasets
categories = ['no_traffic', 'traffic'] #image categories

train_data = []
def create_train_data():
    for category in categories:
        path = os.path.join(directory,category)  #file path for every category folder
        class_num = categories.index(category)  #to put which image in which category
        #print(os.listdir(path))
        for image in os.listdir(path):
            #change the image into an array, change the colors into grayscale
            imgs = cv2.imread(os.path.join(path,image), cv2.IMREAD_GRAYSCALE)
            img_resize = cv2.resize(imgs, (200, 200)) #resize images
            train_data.append([img_resize, class_num]) #put them into the training data
            
create_train_data()
random.shuffle(train_data) #shuffle the train data

#put them into variables to be used in the neural network
X = [] #features (the image's features)
y = [] #labels (where the image is categorized in)

for features, label in train_data:
    X.append(features)
    y.append(label)

#convert X to numpy array and reshape the data according to image size and color scale
X = np.array(X).reshape(-1, 200, 200, 1)

X = X/255.0

print(X.shape[1:])

#save/load the model
np.save('saveX.npy', X)
np.save('saveY.npy', y)
np.load('saveX.npy')
np.load('saveY.npy')
    
