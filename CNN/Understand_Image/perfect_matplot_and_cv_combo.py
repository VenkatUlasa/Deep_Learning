import numpy as np
import matplotlib.pyplot as plt
import cv2

data = plt.imread("images/lena_color_512.tif")

# we need to reverse the layers of the data read by matplotlib to show with openCV .
# it is mandatory to get accurate outcome.

rev_data = data[ : , : , ::-1]
cv2.imshow("my_image" , rev_data)
cv2.waitKey()
cv2.destroyAllWindows()