import cv2
import numpy as np
import os
import pickle

name = ''



def image_detect(frame):
    try:
        id1=0
        global name
        labels = {"person_name": 1}
        face_dir1 = os.path.dirname(os.path.abspath(__file__))
        face_dir = os.path.join(face_dir1 , "haarcascade_frontalface_default.xml")
        print(face_dir)
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        file_dir = os.path.join(BASE_DIR, "recognizer/trainningData.yml")
        label_dir = os.path.join(BASE_DIR, "pickles/face-labels.pickle")
        
        with open(label_dir, 'rb') as f:
            og_labels = pickle.load(f)
            labels = {v:k for k,v in og_labels.items()}
        

        print(file_dir)
        face_cascade = cv2.CascadeClassifier(face_dir)

        rec = cv2.face.LBPHFaceRecognizer_create() 
        rec.read(file_dir)

        font = cv2.FONT_HERSHEY_SIMPLEX
        gray = cv2.cvtColor(frame ,cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray , 1.3, 5)
        if len(faces) != 0:
            for x,y,w,h in faces:
                # cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
                id1,conf=rec.predict(gray[y:y+h,x:x+w])
                print("face id = "+ str(id1))
                if conf>=4 and conf <= 85:
                    name = labels[id1]
                    # name = id1
                else:
                    name = "Unknown"
            cv2.destroyAllWindows()
        else:
            name = "Face Not Detection..."
        return name
    except Exception as e:
        return "vale ="+ str(e)

