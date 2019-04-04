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

while(True):
    ret, frame = capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors = 5,
        minSize = (30,30),
        flags = cv2.CASCADE_SCALE_IMAGE
    )

    for (x,y,w,h) in faces:
        count += 1
        #cv2.rectangle(frame, (x, y), (x+w, y+h), (255,255,255), 2)
        sub_face = frame[y-20:y+h+20, x-20:x+w+20]
        faceFileName = "{}/face".format(databasePath) + str(count) + ".jpg"
        cv2.imwrite(faceFileName, sub_face)
        cv2.waitKey(200)

    cv2.imshow('Frame', frame)
    if count == 25:
        break

print("{} added Successfully".format(rollNo))

capture.release()
cv2.destroyAllWindows()
