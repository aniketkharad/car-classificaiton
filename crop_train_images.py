import os
import csv
import cv2
import numpy as np 

path_base = '../project/stanford-car-dataset-by-classes-folder'
class_names = []
with open(path_base + '/names.csv') as csvNmesFile:
    carNames = csv.reader(csvNmesFile, delimiter = ';')
    for row in carNames:
        if(row[0] == 'Ram C/V Cargo Van Minivan 2012'):
            row[0] = "Ram C-V Cargo Van Minivan 2012"
        class_names.append(row[0])
# This represents the lsit of all the classes of cars given. It totals to 196

anno_train = {}
with open(path_base + '/anno_train.csv') as trainImage:
    trainingImages = csv.reader(trainImage, delimiter = ',')
    for row in trainingImages:
        anno_train[row[0]] = [row[1], row[2], row[3], row[4], row[5]]
# The dictionary of the individual images of training dataset

imageLoc = path_base + '/car_data/car_data/train/'   #The list imageLoc with class names
# imageLocList = os.listdir(imageLoc)
# List of image classes
os.chdir(imageLoc)


for class_ in class_names :
    images_in_class = os.listdir('./{}/'.format(class_))
    os.chdir('./{}/'.format(class_))

    i = 0
    for eachImage in images_in_class :
    #     # print(anno_train[eachImage][4], class_names[int(anno_train[eachImage][4])-1])
        r0 = anno_train[eachImage][0]
        r1 = anno_train[eachImage][1]
        r2 = anno_train[eachImage][2]
        r3 = anno_train[eachImage][3]
        # print(eachImage,r0,r1,r2,r3,r4)

        img = cv2.imread(eachImage)
        imCrop = img[int(r1):int(r3), int(r0):int(r2)]
        cv2.imwrite(eachImage, imCrop)

        i+=1
        fract = i / len(images_in_class)
        print('     {:>2.2%}'.format(fract), end="\r")
    

    # print('Cropped images of\t\t{}'.format(classs_))
    os.chdir('../')
    print('Cropped images of {}'.format(class_))



