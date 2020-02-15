import numpy as np
import cv2
import pickle
import requests
import face_recognition

# refer to opencv_cameratest for detailed explanation of basic underlying code
# note that we need to copy the data folder to the same directory as our code in a folder called cascades
# experiment with different haar cascade models to see how we can grab facial features differently

cap = cv2.VideoCapture(0)

#url = "http://100.80.129.11:8080/shot.jpg"          # specific to IP address, port 8080

encoding_lst = []
label_lst = []

known_image1 = face_recognition.load_image_file("image1.jpg")
known_encoding1 = face_recognition.face_encodings(known_image1)[0]

encoding_lst.append(known_encoding1)
label_lst.append("Boss")

unknown_image = face_recognition.load_image_file("image2.jpg")
unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

face_locations = face_recognition.face_locations(unknown_image)

while True:
    ret, frame = cap.read()

    #img_resp = requests.get(url)                    # stores the image at the URL
    #img_arr = np.array(bytearray(img_resp.content), dtype = np.uint8)   # converting image to numpy array
    #frame = cv2.imdecode(img_arr, -1)               # decoding numpy array into a picture that is readable


    # scaleFactor > 1.5 can improve results but too high is bad

    # h is bottomost coordinate of region of interest (height of roi), w is rightmost coordinate of region of interest (width of roi)
    
    # draws rectangle from (x, y) to (x + w, y + h) of colour 'color', width 'stroke' around region of interest
    color = (255, 0, 0)                     # BGR value - blue colour. You can pick whatever you want of course
    stroke = 2                              # thickness of line. Pick whatever you want
    cv2.rectangle(frame, (face_locations[0][0], face_locations[0][1]), (face_locations[0][2], face_locations[0][3]), color, stroke)

    # Recognising the face. Perfect place to integrate a deep learning model such as keras / tensorflow / pytor / scikit learn
    # The approach below is not foolproof, but does work and is simple. Integrating deep learning models will complicate things

    # recog API stuff

    # problem with approach is confidence varies a lot and goes above 100, so is not actually measuring confidence
    #if conf >= 45 and conf <= 85:
    #   print(id_)                          # prints out training label
    #  print(labels[id_])                  # prints out name associated with training label

    for i in range(len(label_lst)):
        results = face_recognition.face_encodings([encoding_lst[i]], unknown_encoding)
        if results == True:
            # manually adding label to training image
            font = cv2.FONT_HERSHEY_SIMPLEX
            name = label_lst[0]
            color = (255, 0, 0)     # blue
            stroke = 2

            # attributes: source frame, name of label, coordinates, font, font size, color of label, thickness of label stroke
            cv2.putText(frame, name, (face_locations[0][0], face_locations[0][1]), font, 1, color, stroke, cv2.LINE_AA)

            break
        
        img_item = "my_image.png"               
        cv2.imwrite(img_item, face_recognition.face_locations(unknown_image))         # saves region of interest from color frame to file      

    if results == False:
        cv2.putText(frame, "Unknown", (face_locations[0][0], face_locations[0][1]), font, 1, color, stroke, cv2.LINE_AA)

    cv2.imshow('frame', frame)

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()
    