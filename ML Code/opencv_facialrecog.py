import numpy as np
import cv2
import pickle
import requests
import face_recognition

# refer to opencv_cameratest for detailed explanation of basic underlying code
# note that we need to copy the data folder to the same directory as our code in a folder called cascades
# experiment with different haar cascade models to see how we can grab facial features differently

cap = cv2.VideoCapture(0)

# url = "http://100.80.129.11:8080/shot.jpg"          # specific to IP address, port 8080

encoding_lst = []
label_lst = []

known_image1 = face_recognition.load_image_file("image1.jpg")
known_encoding1 = face_recognition.face_encodings(known_image1)[0]

encoding_lst.append(known_encoding1)
label_lst.append("Boss")

unknown_image = face_recognition.load_image_file("image2.jpg")
unknown_encoding = face_recognition.face_encodings(unknown_image)[0]


while True:
    ret, frame = cap.read()

    # img_resp = requests.get(url)                    # stores the image at the URL
    # img_arr = np.array(bytearray(img_resp.content), dtype = np.uint8)   # converting image to numpy array
    # frame = cv2.imdecode(img_arr, -1)               # decoding numpy array into a picture that is readable

    # scaleFactor > 1.5 can improve results but too high is bad

    # h is bottomost coordinate of region of interest (height of roi), w is rightmost coordinate of region of interest (width of roi)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    face_locations = face_recognition.face_locations(gray)
    face_encodings = face_recognition.face_encodings(gray, face_locations)

    for i in range(len(label_lst)):
        results = face_recognition.compare_faces(
            [encoding_lst[i]], face_encodings)

        if results[0] == True:
            cv2.rectangle(gray, (face_locations[3], face_locations[0]), (
                face_locations[1], face_locations[2]), (0, 255, 0), 2)
            cv2.putText(gray, label_lst[i], (face_locations[3] + 5, face_locations[0] + 5, cv2.FONT_HERSHEY_DUPLEX, 2, (0, 255, 0), 2)

        # img_item = "my_image.png"
        # cv2.imwrite(img_item, face_recognition.face_locations(unknown_image))         # saves region of interest from color frame to file

    if results == False:
        cv2.putText(
            gray, "Unknown", (face_locations[0], face_locations[1]), font, 1, color, stroke, cv2.LINE_AA)

    cv2.imshow('frame', frame)

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
