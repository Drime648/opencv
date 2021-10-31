import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('../photos/trck-pic-1.jpg')

cv.imshow('img', img)




#bgr to grayscale

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)


# #bgr to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('hsv', hsv)

# #LAB

lab = cv.cvtColor(img, cv.COLOR_BGR2Lab)
cv.imshow('lab', lab)



#cv.waitKey(0)