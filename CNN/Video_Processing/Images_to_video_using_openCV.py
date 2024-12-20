import numpy as np
import cv2
import glob

images_path = "D:\DEEP LEARNING PRACTICE\CNN\PracticeFile\Frames"

image_files = glob.glob(f"{images_path}/*.jpg") + glob.glob(f"{images_path}/*.png")
image_files.sort()

first_frame = cv2.imread(image_files[0])
height = first_frame.shape[0]
width = first_frame.shape[1]

video=cv2.VideoWriter('D:/DEEP LEARNING PRACTICE/CNN/PracticeFile/new_video.mp4',cv2.VideoWriter_fourcc(*'mp4v'),30,(width,height))

for i in image_files :
    a = cv2.imread(i)

    b = cv2.resize(a , (width , height))

    video.write(b)

video.release()