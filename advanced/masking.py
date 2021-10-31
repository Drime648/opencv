import cv2 as cv
import numpy as np


img = cv.imread('../photos/trck-pic-1.jpg')
cv.imshow('img', img)

blank = np.zeros(img.shape[:2], np.uint8)

cv.imshow('blank', blank)


mask = cv.circle(blank, (img.shape[1] // 2, img.shape[0]//2 ), 100, 255, -1)
cv.imshow("mask", mask)


masked_img = cv.bitwise_and(img, img, mask=mask)
cv.imshow("masked image", masked_img)


#masking puts a shape on top of the image



cv.waitKey(0)