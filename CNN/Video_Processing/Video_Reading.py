import numpy as np
import matplotlib.pyplot as plt
import cv2
import datetime

cap = cv2.VideoCapture("images/sample_video.mp4")

count = 0

while True :
    status , pixels = cap.read()
    if status == True :
        count += 1
        d_time = datetime.datetime.now()
        text = d_time.strftime("%c")
        font = cv2.FONT_HERSHEY_PLAIN
        cv2.putText(pixels , text , (50,50) , font , 1 , (0,0,0) , 2)
        cv2.imshow("image" , pixels)
        if cv2.waitKey(20) == ord("q") :
            break
    else :
        break
print(count)
cap.release()
cv2.destroyAllWindows()