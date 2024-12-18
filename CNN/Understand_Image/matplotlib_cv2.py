import numpy as np
import matplotlib.pyplot as plt
import cv2

# Here we are going to read the image with "Matplotlib"
# showing with "OpenCV"
# it will give same image but there will be change in color of the result image

im_data = plt.imread("images/lena_color_512.tif")
print(im_data)

cv2.imshow("result_image" , im_data)
# it will give image with some other color
# because we know that matplotlib reads -> [R , G , B]  and CV reads -> [B , G , R]
cv2.waitKey()
cv2.destroyAllWindows()