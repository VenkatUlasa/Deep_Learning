
import numpy as np
import matplotlib.pyplot as plt
import cv2

# callback function
def c_fun(EVENT , x,y,a,b) :
    # EVENT -> nothing but the the event occured by the mouse.
    if EVENT == cv2.EVENT_LBUTTONDOWN :
        text = str(x) + "," + str(y)
        font = cv2.FONT_HERSHEY_PLAIN
        cv2.putText(im_data , text , (x,y) , font , 1 , (0,0,0) , 2)
        cv2.imshow("Lina_image" , im_data)

im_data = cv2.imread("images/lena_color_512.tif")

cv2.imshow("Lina_image" , im_data)


cv2.setMouseCallback("Lina_image" , c_fun)

cv2.waitKey()
cv2.destroyAllWindows()