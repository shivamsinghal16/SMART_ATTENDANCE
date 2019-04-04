import cv2
import numpy as np
import os
from attendanceSheet import createAttendanceSheet

def detect_face(img):
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
	faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5);
	if (len(faces) == 0):
		return None, None
	(x, y, w, h) = faces[0]
	return gray[y:y+w, x:x+h], faces[0]

section=input("Enter Section: ")
model_path="Database/"+ "Section"+ section + ".xml"
face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.read(model_path)
present = []
 
def predict(test_img):
        img = test_img.copy()
        face, rect = detect_face(img)
        label= face_recognizer.predict(face)
        label_text = str(label[0])
        if(label[1]<60):
                present.append(int(label_text))
        return img

dirs=os.listdir("ClassImage")

for image in dirs:
	test_img1 = cv2.imread("ClassImage/"+image)
	predicted_img1 = predict(test_img1)

cv2.waitKey(0)
cv2.destroyAllWindows()
present.sort()
createAttendanceSheet(present)
