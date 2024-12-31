import cv2
import numpy as np

maths = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
vv = cv2.VideoCapture("obama.mp4")

while True :
    sta , image = vv.read()
    if sta == True :
        cordinates, num_of_faces = maths.detectMultiScale2(image)
        if len(cordinates) > 0 :
            x1 = cordinates[0][0]
            y1 = cordinates[0][1]
            x2 = cordinates[0][2]
            y2 = cordinates[0][3]
            cv2.rectangle(image, (x1, y1), (x2 + x1, y2 + y1), (0, 0, 255), 2)
            cv2.imshow("image",image)
            if cv2.waitKey(20) == ord("q"):
                break
    else:
        break
vv.release()
cv2.destroyAllWindows()
