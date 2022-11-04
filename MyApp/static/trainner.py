import cv2
import os
import numpy as np
from PIL import Image

def  trainingImage():
	try:
		face_dir1 = os.path.dirname(os.path.abspath(__file__))
		face_dir = os.path.join(face_dir1 , "haarcascade_frontalface_default.xml")
		print(face_dir)
		face_cascade = cv2.CascadeClassifier(face_dir)
		recognizer = cv2.face.LBPHFaceRecognizer_create()

		BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
		image_dir = os.path.join(BASE_DIR, "media")

		rec_dir = os.path.dirname(os.path.abspath(__file__))
		recog_dir = os.path.join(rec_dir, "recognizer\\trainningData.yml")
		print(recog_dir)
	

		y_labels = []
		x_train = []

		for root, dirs, files in os.walk(image_dir):
			for file in files:
				if file.endswith("png") or file.endswith("jpg"):
					path = os.path.join(root, file)
					label = os.path.basename(root).replace(" ", "-").lower()
					pil_image = Image.open(path).convert("L") # grayscale
					image_array = np.array(pil_image, "uint8")
					faces = face_cascade.detectMultiScale(image_array, scaleFactor=1.3, minNeighbors=5)
					print(path)
					print(faces)
					for (x,y,w,h) in faces:
						roi = image_array[y:y+h, x:x+w]
						x_train.append(roi)
						y_labels.append(int(label))
		recognizer.train(x_train, np.array(y_labels))
		recognizer.save(recog_dir)
		return "Successfully Image Train.."
	except Exception as e:
		return e