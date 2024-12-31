import numpy as np
import cv2

image = cv2.imread('mul.jpg') # reading the image
maths = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cordinates,num_of_faces = maths.detectMultiScale2(image)

print(len(num_of_faces))
print(cordinates)
c = 1
for i in range(len(num_of_faces)):
    c += 1
    x1 = cordinates[i][0]
    y1 = cordinates[i][1]
    x2 = cordinates[i][2]
    y2 = cordinates[i][3]

    cv2.rectangle(image,(x1,y1),(x2+x1,y2+y1),(0,0,255),2)
    cv2.putText(image , str(c) , (x1+10,y1+20) , cv2.FONT_HERSHEY_PLAIN , 1 , (0,255,0) , 2)

cv2.imshow('single',image)
cv2.waitKey()
cv2.destroyAllWindows()