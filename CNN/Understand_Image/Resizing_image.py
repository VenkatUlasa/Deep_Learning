import numpy as np
import cv2

data = cv2.imread("images/lena_color_512.tif")
print(f'Original image shape :  {data.shape}')

resized_image = cv2.resize(data , dsize= (256,256))
# actually the size of the image is (512 , 512)
# we are converting the image size into (256,256) by using " resize() "

print(f'Original image shape :  {resized_image.shape}')

cv2.imshow("normal_image" , data)
cv2.imshow("resized_image" , resized_image)
cv2.waitKey()
cv2.destroyAllWindows()
