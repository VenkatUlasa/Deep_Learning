import numpy as np
import matplotlib.pyplot as plt
import cv2

im1 = cv2.imread("images/lena_color_512.tif")

im2 = cv2.imread("images/mandril_color.tif")

new_image_add = cv2.add(im1 , im2)
addWeight_image = cv2.addWeighted(im1,0.7 , im2 , 0.3 , 1 )

cv2.imshow("merged_image_add" , new_image_add)
cv2.imshow("addWeight_image" , addWeight_image)
cv2.waitKey()
cv2.destroyAllWindows()

