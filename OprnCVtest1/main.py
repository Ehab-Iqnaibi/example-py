import cv2 as cv
import numpy as np

img = cv.imread('C:/Users/Ehab M F Iqnaibi/Pictures/course/f1.jpg', cv.IMREAD_COLOR)
size = img.shape
print(size)
neg_img = np.zeros(size, np.uint8)
for i in range(size[0]):
  for j in range(size[1]):
    in_pixel = img[i, j]
    out_pixel = [255-in_pixel[0], 255-in_pixel[1], 255-in_pixel[2]]
    neg_img[i, j] = out_pixel

cv.imshow('input',neg_img)