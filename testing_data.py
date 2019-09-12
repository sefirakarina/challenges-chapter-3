# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 13:10:22 2018

@author: sefira karina

references:
https://www.youtube.com/watch?v=wQ8BIBpya2k&list=PLQVvvaa0QuDfhTox0AjmQ6tvTgMBZBEXN
"""

#NOTE : Please make sure you have the trained_model6.h5 in the same folder as this file
#	    if you don't have the trained model yet, download it in https://mega.nz/#!zygnUSra!Fvw1sFiO9PKnWZ7Ya-sgzDqCIjZZSfGyCUg2pb4041o
#       if you want to make your own model, run loading_data.py to load data, then run train_data.py to get the training file

from keras.models import load_model
import cv2
import tensorflow as tf
from PIL import Image

categories = ['no_traffic', 'traffic']

#ask user to input image path they want to predict
input_path = input('image path: ')#'image\macet.jpg'

Image.open(input_path)

#adjust the image the same way as we adjust the data in loading_data.py
def adjust(path):
    img_arr = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    new_arr = cv2.resize(img_arr, (200, 200))
    new_arr = new_arr/255.0
    return new_arr.reshape(-1, 200, 200, 1)

#load the model from the file produced by train_data.py
model = tf.keras.models.load_model("trained_model6.h5")


#predict the image
ans = model.predict_classes([adjust(input_path)])

#input_path.show()
print(ans)
print(categories[int(ans)])
#print(categories[int(ans[0][0])])