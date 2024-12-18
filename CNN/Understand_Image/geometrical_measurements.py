import numpy as np
import cv2

data = cv2.imread("images/lena_color_512.tif")

# cv2.line(data , point1 , point2) ; point : (x , y)

# cv2.line(data , (150 , 200) , (430,490) ,color=(0,255,0) , thickness=10)
#            above line used to draw a line by adding two points.

# cv2.arrowedLine(data , (150 , 200) , (430,490) ,color=(0,255,0) , thickness=10)
#            above line used to draw a arrowed line by adding two points.

# cv2.rectangle(data , (150 , 200) , (430,490) ,color=(0,255,0) , thickness=10)
#            above line used to draw a rectangle by adding two points.

# cv2.rectangle(data , (150 , 200) , (430,490) ,color=(0,255,0) , thickness=-1)
#            above line used to draw a masked rectangle by adding two points. by using thickness "-1".

# cv2.circle(data , (250 , 250) , radius=200 ,color=(0,255,0) , thickness=10)
#            above line used to draw a circle from the given point with given radius.

cv2.circle(data , (250 , 250) , radius=200 ,color=(0,255,0) , thickness= -1)
#            above line used to draw a masked circle from the given point with given radius.

cv2.imshow("image",data)
cv2.waitKey()
cv2.destroyAllWindows()