# car-classificaiton
## Model classifies cars based on name, model, year. Predicts its confidence amongst 20 different cars' used in training. 

Using neural network (feed forward) to classifiy cars by their { name; model; year }

The dataset is available at kaggle. The repository name is "Stanford Cars Dataset" and can be directly downloaded by the link given below or by visiting the kaggle site as

web page -- "https://www.kaggle.com/jessicali9530/stanford-cars-dataset"

### direct download -- "https://www.kaggle.com/jessicali9530/stanford-cars-dataset/download"

This can also be downloaded by using the link here -- "https://ai.stanford.edu/~jkrause/cars/car_dataset.html" Once it has been downloaded and extracted in a directory, the python scripts given for selecting and croping the cars out of the image sets help in reducing the size of the image as well as imporving in reducing noise generated from the surrrounding.

The 2 .py scripts are crop_train_images.py and crop_test_images.py

After the data is preprocesed it can be used for traning and testinng of different machines..

Here I have used few (20) classes of images form both testing and traing directories and merged to form a single class of cars for traning and evaluation of the feed forwad neural network..
