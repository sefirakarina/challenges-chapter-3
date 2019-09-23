# traffic-predictor-keras

<img src="https://github.com/sefirakarina/challenges-chapter-11/blob/master/Capturet.PNG" width="500">
## Please download the trained model first from the following, or else the program won't run well.

[link to the model](https://mega.nz/#!zygnUSra!Fvw1sFiO9PKnWZ7Ya-sgzDqCIjZZSfGyCUg2pb4041o)

Put the things in the downloaded folder in the repository you've pulled (put them on the same folder as the python files)

### To run this program, the following things are required
- Python 3.6 (tensorflow doesn't support python 3.7 yet)
- keras
- theanos
- tensorflow
- numpy
- PIL (python library)

### How to start the program
- go to terminal, cd to the cloned repository
- type the following command
```bash
python tryapp.py
```
- wait for it to load until it tells you **Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)**

<img src="https://github.com/sefirakarina/challenges-chapter-11/blob/master/cgrun.PNG" width="700"/>

- then open your browser and go to http://localhost:5000/
- click choose image, and make sure you choose image from the folder 'static' inside the repository
- then click submit to predict.

### Concept
I use convolutional neural network (CNN), which is a part of deep neural network to differentiate the difference between road with traffic jam and clear road. The idea is to make a program that can update user immediately whether there is traffic or not by recognizing the condition of the road. CNN takes an input image, process it and classify it as the given categories. In CNN, the input image that has been processed will be trained, and tested with the layers. In this program, I use convolutional layer, pooling layer, flatten the feature produced from the pooling, and finally end it with the fully connected layer. The details can be seen in the following section.

### Architecture
<img src="https://github.com/sefirakarina/challenges-chapter-11/blob/master/cg9.PNG" width="800"/>

# loading_data.py
After gathering the images, in this part these images are going to be loaded to the network so it can train the data. First the images are categorized, which in this case, into two categories, no_traffic and traffic, which is classified by the categories’ index numbers. The images are then converted to an array and sets the color to grayscale because RGB images have larger size than grayscale and grayscale images are faster to process. The images are then resized so each image have size 200x200 pixels so all of the images will have the same shape and size. After that the images are put into the training data then they are shuffled so the image won’t come out in order of the image and the category. The data is then put to the variables that are going to be used before giving it to the neural network to be built into lists, and then reshape them according to the shape of the images and the number of color channels (in this case 1 because grayscale is used), and then scaled so it can be processed. They are then saved to a numpy file so the dataset doesn’t have to be rebuilt when the neural network wants to be used again.

# train_data.py
In this part, make the layers. In this case the layers used are Conv2D, MaxPooling2D, Dense, and Flatten. Further explanation of these layers can be found on the previous part of this report. Then, configure the model. After that, load the dataset and its validation from the numpy arrays that was saved from loading_data.py, and train the data with the model, and save the model into a file, so it can be used again later on. Here’s the summary of the model I made:

<img src="https://github.com/sefirakarina/challenges-chapter-11/blob/master/cgtrain.PNG" width="500"/>

# tryapp.py
The first thing this part do is load the saved model from the previous part to be used to test other image. This part makes it possible for user to choose and upload their own image to be predicted. To do that, flask API is used to post the image from html (index3.html). As soon as the user upload the image and click submit, the data will be sent to the python backend. And it will be processed the same way as the trained dataset, then with the saved model from train_data.py, predict the image class, and show the output along with the image in the html page.

# experiment.py
In this file, a total of 42 images (21 traffic and 21 no traffic) are tested with the trained model. The testing accuracy of the 42 images provided is 88.05% with 37 out of 42 images predicted correctly.

## Experiments or tests 
The dataset consists of around 180 pictures of each traffic and non traffic data. The data was trained with epoch of 29 (accuracy 93%), because it overfitted at around epoch 30.

<img src="https://github.com/sefirakarina/challenges-chapter-11/blob/master/cgex1.PNG" width="500"/>

Here’s the summary of the model:

<img src="https://github.com/sefirakarina/challenges-chapter-11/blob/master/cgex2.PNG" width="500"/>

Then, in the file experiment.py, a total of 42 images were used to test the trained model (21 traffic, 21 no traffic). The result is as following:

<img src="https://github.com/sefirakarina/challenges-chapter-11/blob/master/cgex3.PNG" width="400"/>

As it can be seen from the image above, the testing accuracy of the 42 images provided is 88.095% with 37 out of 42 images predicted correctly.

