
import numpy as np
import matplotlib.pyplot as plt
import cv2

# callback function
def c_fun(EVENT , x,y,a,b) :
    # EVENT -> nothing but the the event occured by the mouse.
    if EVENT == cv2.EVENT_LBUTTONDOWN :
        b = im_data[x,y,0]
        g = im_data[x,y,1]
        r = im_data[x,y,2]
        text = str(b) + "," + str(g) + ","+str(r)
        font = cv2.FONT_HERSHEY_PLAIN
        cv2.putText(white_image , text , (x,y) , font , 1 , (10,10,255) , 2)
        cv2.imshow("white_image" , white_image)

im_data = cv2.imread("images/lena_color_512.tif")
white_image = np.zeros((512,512,3))

cv2.imshow("Lina_image" , im_data)
cv2.imshow("white_image" , white_image)


cv2.setMouseCallback("Lina_image" , c_fun)

cv2.waitKey()
cv2.destroyAllWindows()