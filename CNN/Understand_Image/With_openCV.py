import numpy as np
import cv2

data = cv2.imread("images/lena_color_512.tif" , 1)

cv2.imshow("image" , data)  # it shows the image and closes immediately
cv2.waitKey()  # to maintain the image popup on screen

cv2.destroyAllWindows()  # with using this we can remove the popup on screen by clicking any key in keyboard.



