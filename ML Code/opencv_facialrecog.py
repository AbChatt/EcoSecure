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

known_encoding_lst = []
label_lst = []
unknown_encoding_lst = []
unknown_labels_lst = []

known_image1 = face_recognition.load_image_file("image1.jpg")
known_encoding1 = face_recognition.face_encodings(known_image1)[0]

known_encoding_lst.append(known_encoding1)
label_lst.append("Boss")

while True:
    ret, frame = cap.read()

    #img_resp = requests.get(url)                    # stores the image at the URL
    #img_arr = np.array(bytearray(img_resp.content), dtype = np.uint8)   # converting image to numpy array
    #frame = cv2.imdecode(img_arr, -1)               # decoding numpy array into a picture that is readable

    RGB_frame = frame[:, :, ::-1]

    face_locations = face_recognition.face_locations(RGB_frame)
    face_encodings = face_recognition.face_encodings(RGB_frame, face_locations)

    for unknown_encode in unknown_encoding_lst:
        results = face_recognition.compare_faces(known_encoding_lst, unknown_encode)
        name = "Unknown"

        if True in results:
            index = results.index(True)
            name = label_lst[index]
        
        unknown_labels_lst.append(name)

    for i in range(len(unknown_labels_lst)):
        cv2.rectangle(frame, (face_locations[i][3], face_locations[i][0]), (face_locations[i][1], face_encodings[i][2]), (255, 0, 0), 2)

        cv2.rectangle(frame, (face_locations[i][3], face_locations[i][0] - 10), (face_locations[1], face_locations[2]), (255, 0, 0), 2)
        cv2.putText(frame, unknown_labels_lst[i], (face_locations[i][3] + 3, face_locations[i][0] - 3), cv2.FONT_HERSHEY_DUPLEX, 2, (255, 254, 253), 2)
    
        img_item = "my_image.png"
        cv2.imwrite(img_item, face_recognition.face_locations(frame))

    cv2.imshow('frame', frame)

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
