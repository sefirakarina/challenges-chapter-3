"""
Created on Thu Dec 26 13:03:15 2018

@author: Sefira Karina

references:
https://www.youtube.com/watch?v=wQ8BIBpya2k&list=PLQVvvaa0QuDfhTox0AjmQ6tvTgMBZBEXN
https://flask-restful.readthedocs.io/en/latest/
https://blog.keras.io/building-a-simple-keras-deep-learning-rest-api.html
"""

#NOTE : Please make sure you have the trained_model6.h5 in the same folder as this file
#       if you don't have the trained model yet, download it in https://mega.nz/#!zygnUSra!Fvw1sFiO9PKnWZ7Ya-sgzDqCIjZZSfGyCUg2pb4041o
#       if you want to make your own model, run loading_data.py to load data, then run train_data.py to get the training file

import flask
from flask import render_template, redirect, Flask
from flask import request, url_for, render_template, redirect
from keras import backend as kb
from keras.models import load_model
import cv2
import tensorflow as tf
from PIL import Image

app = Flask(__name__)

#function to adjust input image to be predicted
def adjust(path):
    img_arr = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    new_arr = cv2.resize(img_arr, (200, 200))
    return new_arr.reshape(-1, 200, 200, 1)


@app.route('/', methods=["GET", "POST"])
def index():
    categories = ['no_traffic', 'traffic']
    arr = None
    global ans
    ori_input_file_name = "whiteqm2.png" #default image that the user will see
    if request.method == "POST": #receive image from html
        if flask.request.files.get("image"):
            input_file = flask.request.files["image"]
            ori_input_file_name = input_file.filename
            input_file_name = "static/"+ input_file.filename
            #load the model
            model = tf.keras.models.load_model("trained_model6.h5")
            try: #predict the image withe the trained model
                ans = model.predict_classes([adjust(input_file_name)])
                arr = {"prediction": categories[int(ans)]}
            except:
                ans = "ERROR, PLS RESTART PROGRAM AND CHOOSE IMAGE FROM THE 'STATIC' FOLDER"
                arr = {"prediction": ans}

            kb.clear_session()
            ans = None
            tf.keras.backend.clear_session()
    return render_template('index3.html', arr=arr, img_name=ori_input_file_name)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

