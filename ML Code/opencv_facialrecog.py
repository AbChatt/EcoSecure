import numpy as np
import cv2
import pickle
import requests
import face_recognition

# refer to opencv_cameratest for detailed explanation of basic underlying code
# note that we need to copy the data folder to the same directory as our code in a folder called cascades
# experiment with different haar cascade models to see how we can grab facial features differently

#recognizer = cv2.face.LBPHFaceRecognizer_create()       # can use a different recogniser - such as a deep learning model
face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')  # calling the appropriate face model
#eye_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_eye.xml')    # calling the appropriate eye model
#smile_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_smile.xml')    # calling the appropriate smile model

#recognizer.read("trainer.yml")                          # read from training model

#labels = {}
#with open("labels.pickle", 'rb') as f:                  # reading label ids from file as bytes
#    og_labels = pickle.load(f)
#    labels = {v:k for k, v in og_labels.items()}          # inverting key value relationship of dictionary - so we can get name

cap = cv2.VideoCapture(0)

#url = "http://100.80.129.11:8080/shot.jpg"          # specific to IP address, port 8080

encoding_lst = []
label_lst = []

known_image1 = face_recognition.load_image_file("image1.jpg")
known_encoding1 = face_recognition.face_encodings(known_image1)[0]

encoding_lst.append(known_encoding1)
label_lst.append("Boss")

while True:
    ret, frame = cap.read()

    #img_resp = requests.get(url)                    # stores the image at the URL
    #img_arr = np.array(bytearray(img_resp.content), dtype = np.uint8)   # converting image to numpy array
    #frame = cv2.imdecode(img_arr, -1)               # decoding numpy array into a picture that is readable

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Model must be trained on grayscale version of video feed (documentation guidelines)

    # scaleFactor > 1.5 can improve results but too high is bad
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)   # values from documentation. Experiment to get best results

    # h is bottomost coordinate of region of interest (height of roi), w is rightmost coordinate of region of interest (width of roi)
    for (x, y, w, h) in faces:                  # prints all the values from face (region of interest) in frame
        #print(x, y, w, h)
        #roi_gray = gray[y:y + h, x:x + w]       # region of interest for gray frame
        roi_color = frame[y:y + h, x:x + w]     # region of interest for colour frame. Same region as colour frame (of course)

        # Recognising the face. Perfect place to integrate a deep learning model such as keras / tensorflow / pytor / scikit learn
        # The approach below is not foolproof, but does work and is simple. Integrating deep learning models will complicate things

        # recog API stuff

        face_locations = face_recognition.face_locations(frame)

        unknown_encoding = face_recognition.face_encodings(frame)[0]

        results = face_recognition.compare_faces([known_encoding1], unknown_encoding)

        # need a lot of images and data to make this model somewhat good

        #id_, conf = recognizer.predict(roi_gray)    # predicting the region of interest (giving us the label and confidence of pred)

        # problem with approach is confidence varies a lot and goes above 100, so is not actually measuring confidence
        #if conf >= 45 and conf <= 85:
         #   print(id_)                          # prints out training label
          #  print(labels[id_])                  # prints out name associated with training label

        if results == True:
            # manually adding label to training image
            font = cv2.FONT_HERSHEY_SIMPLEX
            name = label_lst[0]
            color = (255, 0, 0)     # blue
            stroke = 2

            # attributes: source frame, name of label, coordinates, font, font size, color of label, thickness of label stroke
            cv2.putText(frame, name, (x, y), font, 1, color, stroke, cv2.LINE_AA)

        # possible issues: image sizes, not real representation, wrong conf interval
        
        img_item = "my_image.png"               
        cv2.imwrite(img_item, roi_color)         # saves region of interest from color frame to file

        # draws rectangle from (x, y) to (x + w, y + h) of colour 'color', width 'stroke' around region of interest
        color = (255, 0, 0)                     # BGR value - blue colour. You can pick whatever you want of course
        stroke = 2                              # thickness of line. Pick whatever you want
        height = y + h
        width = x + w
        cv2.rectangle(frame, (x, y), (width, height), color, stroke)

        #eyes = eye_cascade.detectMultiScale(roi_gray)   # same as the face recognition, but for eye tracking
        
        #subitems = smile_cascade.detectMultiScale(roi_gray)    # same as eye tracking, but for smile recognition

        #for (ex, ey, ew, eh) in eyes:
        #   cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)  # draw rectangle around eyes
        
        #for (sx, sy, sw, sh) in sub_items:
         #   cv2.rectangle(roi_gray, (sx, sy), (sx + sw, sy + sh), (0, 255, 0), 2)   # draw rectangle around smile
        
        # note that smile recognition is horrendous. If we have too much training data for one, it skews the results

    cv2.imshow('frame', frame)

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
    
    cap.release()
    cv2.destroyAllWindows()
    