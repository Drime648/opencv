import cv2 as cv
import numpy as np


img = cv.imread('../photos/trck-pic-1.jpg')

cv.imshow('img', img)

blank = np.zeros(img.shape, dtype=np.uint8)


gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

blur = cv.GaussianBlur(gray, (1,1), cv.BORDER_DEFAULT)


canny = cv.Canny(blur, 125, 175)
cv.imshow('canny', canny)

ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY) #binarize img



contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(len(contours))

cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow('contours', blank)





cv.waitKey(0)