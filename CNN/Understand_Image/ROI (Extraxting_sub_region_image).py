'''
here we are extracting the peace of image from the original image and pasting it into another place in the
image by using mouse handling events to get select the region
'''
import numpy as np
import cv2

# def c_fun(EVENT , x,y , a, b) :
#     if EVENT == cv2.EVENT_LBUTTONDOWN :
#         text = str(x)+","+str(y)
#         font = cv2.FONT_HERSHEY_PLAIN
#         cv2.putText(im_data ,text ,  (x,y) , font , 1 , (0,0,0) ,2)
#         cv2.imshow("original_image" , im_data)


# (x1,y1) => (879,444) ; (x2,y2) => (1298,773)
# above points got by using mouse handling events

im_data = cv2.imread("images/iStock-187164601-e1507133295972.jpg")
cv2.imshow("original_image" , im_data)

sub_resion = im_data[444:773 , 879:1298 ]  # intrested reason
im_data[435:435+(773-444) , 138 : 138+(1298-879) ] = sub_resion  # replaced a part of image with sub reason.

cv2.imshow("sub_resion" , im_data)

# cv2.setMouseCallback("original_image" , c_fun)

cv2.waitKey()
cv2.destroyAllWindows()