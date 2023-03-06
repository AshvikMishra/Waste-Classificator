# About the Project
This is a project forked from the [antiplasti github repository](https://github.com/antiplasti/Plastic-Detection-Model).

A generic image detection program that uses Google's Machine Learning library, [Tensorflow](https://www.tensorflow.org/) and a pre-trained Deep Learning Convolutional Neural Network model called [Inception](https://research.googleblog.com/2016/03/train-your-own-image-classifier-with.html).

Inception was used in the Large Visual Recognition CHallege using data from 2012 and can differentiate between 1000 classes The program applies Transfer Learning to this existing model and re-trains it to classify a new set of images. Essentially, this model can be used to classify any kind of image.

The output is in the form of a probability of what the algorithm thinks the object would be. I have used tkinter for to user to input their image from files and then displayed both the probability and the image as the result.

# How to run the code
Make sure you have [Python 3](https://www.python.org/downloads/) installed, then install [Tensorflow](https://www.tensorflow.org/install/) on your system, and clone this repo.

Unzip the training_dataset.zip file. It should look something like this:
![screenshot](https://user-images.githubusercontent.com/111407501/223183207-1262d2fd-e0c0-42f5-8977-593f703c71c2.png)
with the individual images in each folder

Then, run this cmd in git:
```javascript
$ bash train.sh
```

Finally to run the code, run the cmd:
```javascript
py app.py
```