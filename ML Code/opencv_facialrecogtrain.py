# converts images into trainable data. Make sure you have images stored in the same directory as code in folder called "images"
import os
import numpy as np
import cv2
import pickle

from PIL import Image

# need to make sure each set of images is in a folder named as the label that we will use to identify an image
# Images can be named to be whatever they want, but must not have multiple faces in them

BASE_DIR = os.path.dirname(os.path.abspath(__file__))   # get path where this code is saved
image_dir = os.path.join(BASE_DIR, "images")            # find images folder in folder where code is saved

face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml') # calling the appropriate model
recognizer = cv2.face.LBPHFaceRecognizer_create()       # can use a different recogniser - such as a deep learning model

current_id = 0
label_ids = {}
y_labels = []
x_train = []

for root, dirs, files in os.walk(image_dir):            # prints out path of all image files (of PNG and JPEG format)
    for file in files:
        if file.endswith("png") or file.endswith("jpg"):
            path = os.path.join(root, file)

            # replace all spaces with dashes (if file named incorrectly). these are safeguards
            label = os.path.basename(os.path.dirname(path)).replace(" ", "-").lower()   # can replace dirname(path) with dirname(root)       

            #print(label, path)

            if not label in label_ids:                  # assign ids to correspond to labels
                label_ids[label] = current_id
                current_id += 1
            
            id_ = label_ids[label]
            #print(label_ids)

            # logical assumption but not valid
            #y_labels.append(label)  # this is some number
            #x_train.append(path)    # verify image, then convert to numpy array and then make grayscale to help model

            # converts every pixel in grayscale version of every image to a numpy array
            pil_image = Image.open(path).convert("L")   # converts image to grayscale

            size = (550, 550)                           # resize the image
            final_image = pil_image.resize(size, Image.ANTIALIAS)   # avoid weird artifacts from resizing
            
            image_array = np.array(final_image, "uint8")
            #print(image_array)

            faces = face_cascade.detectMultiScale(image_array, scaleFactor=1.5, minNeighbors=5)   # same as before, or could use default values

            for (x, y, w, h) in faces:
                roi = image_array[y: y + h, x:x + w]    # region of interest
                x_train.append(roi)
                y_labels.append(id_)                    # underscore is important

#print(y_labels)
#print(x_train)

with open("labels.pickle", 'wb') as f:                  # writing label ids to file as bytes. Now we can use them in our facialrecog file
    pickle.dump(label_ids, f)

recognizer.train(x_train, np.array(y_labels))           # not sure if have to convert y to np array in this step, could do it earlier
recognizer.save("trainer.yml")                          # must save to a .yml file
