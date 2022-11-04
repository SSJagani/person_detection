import cv2
import os
import numpy as np
from PIL import Image
import pickle

def  trainingImage():
	try:
		face_dir1 = os.path.dirname(os.path.abspath(__file__))
		face_dir = os.path.join(face_dir1 , "haarcascade_frontalface_default.xml")
		face_cascade = cv2.CascadeClassifier(face_dir)
		recognizer = cv2.face.LBPHFaceRecognizer_create()

		BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
		image_dir = os.path.join(BASE_DIR, "media")

		rec_dir = os.path.dirname(os.path.abspath(__file__))
		Name_file = os.path.join(rec_dir,"pickles\\face-labels.pickle")
		recog_dir = os.path.join(rec_dir, "recognizer\\trainningData.yml")
		# print(recog_dir)
	

		current_id = 0
		label_ids = {}
		y_labels = []
		x_train = []

		for root, dirs, files in os.walk(image_dir):
			for file in files:
				if file.endswith("png") or file.endswith("jpg"):
					path = os.path.join(root, file)
					label = os.path.basename(root).replace(" ", "-").lower()
					#print(label, path)
					if not label in label_ids:
						label_ids[label] = current_id
						current_id += 1
					id_ = label_ids[label]
					pil_image = Image.open(path).convert("L") # grayscale
					image_array = np.array(pil_image, "uint8")
					faces = face_cascade.detectMultiScale(image_array, scaleFactor=1.2, minNeighbors=5)
					print(path)
					print(faces)
					for (x,y,w,h) in faces:
						roi = image_array[y:y+h, x:x+w]
						x_train.append(roi)
						y_labels.append(id_)
		with open(Name_file, 'wb') as f:
			pickle.dump(label_ids, f)
		recognizer.train(x_train, np.array(y_labels))
		recognizer.save(recog_dir)
		return "Successfully Image Train.."
	except Exception as e:
		return e


val = trainingImage()
print(val)