import numpy as np
import matplotlib.pyplot as plt
import cv2
import datetime

im_data = cv2.imread("images/lena_color_512.tif")

date_time = datetime.datetime.now()
text_data = date_time.strftime("%c")
font = cv2.FONT_HERSHEY_TRIPLEX         # we can take any style of font
cv2.putText(im_data , text_data , (50,50) ,font, 1 ,  (0,0,0) , 2)

cv2.imshow("with_text",im_data)
cv2.waitKey()
cv2.destroyAllWindows()