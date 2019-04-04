import cv2

cascPath = "haarcascades/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)

capture = cv2.VideoCapture(0)

def cropFaces(image):
    count = 0

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
        #cv2.rectangle(image, (x, y), (x+w, y+h), (255,255,255), 1)
        sub_face = image[y-20:y+h+20, x-20:x+w+20]
        faceFileName = "E:/SmartAttendance/ClassImage/classimage{}.jpg".format(count)
        cv2.imwrite(faceFileName, sub_face)

    print("Total No. of Students Present: {}".format(count))

while(True):
    ret, frame = capture.read()

    cv2.imshow('Frame', frame)

    k = cv2.waitKey(1)

    if k == ord('c'):
        cropFaces(frame)
        break

capture.release()
cv2.destroyAllWindows()
