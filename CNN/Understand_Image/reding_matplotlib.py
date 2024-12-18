import numpy as np
import matplotlib.pyplot as plt


# Gray Image

data = plt.imread("images/lena_gray_512.tif")
print(data)

plt.imshow(data , cmap = "gray")


# Color Image

data = plt.imread("images/woman_blonde.tif")
print(data)

plt.imshow(data)
plt.show()

