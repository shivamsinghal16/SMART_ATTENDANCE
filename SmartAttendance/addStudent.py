import os
import sys
import cv2
import sqlite3

name = input("Enter Student Name: ")
rollNo = int(input("Enter University Roll No.: "))
section = input("Enter Section: ")

students = os.listdir("E:/SmartAttendance/Database/{}".format(section))

if str(rollNo) in students:
    print("Student is already added")
    sys.exit()
else:
    os.mkdir("E:/SmartAttendance/Database/{}/{}".format(section,rollNo))
    databasePath = "E:/SmartAttendance/Database/{}/{}".format(section,rollNo)

def addToDatabase(rollNo, name):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    cursor.execute('INSERT INTO students values(?,?)',(rollNo,name))
    connection.commit()
    connection.close()

addToDatabase(rollNo,name)

cascPath = "haarcascades/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)

capture = cv2.VideoCapture(0)

count = 0

def cropFace(image):
    global count

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    for (x,y,w,h) in faces:
        count += 1
        #cv2.rectangle(image, (x, y), (x+w, y+h), (255,255,255), 2)
        sub_face = image[y-20:y+h+20, x-20:x+w+20]
        faceFileName = "{}/face".format(databasePath) + str(count) + ".jpg"
        cv2.imwrite(faceFileName, sub_face)

while(True):
    ret, frame = capture.read()

    cv2.imshow('Frame', frame)

    k = cv2.waitKey(1)

    if k == ord('c'):
        if count<25:
            cropFace(frame)
        else:
            print("{} added Successfully".format(rollNo))
            break

capture.release()
cv2.destroyAllWindows()
