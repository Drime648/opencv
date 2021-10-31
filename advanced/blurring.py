import cv2 as cv

import numpy as np


img = cv.imread('../photos/trck-pic-1.jpg')
cv.imshow('img', img)


# averaging
avg = cv.blur(img, (3,3))
cv.imshow('average blur', avg)

# Gaussian blur
gauss = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('gaussian blur', gauss)

# median blurring - like a "smudge", use low kernel size
med = cv.medianBlur(img, 3)
cv.imshow("median blur", med)

#bilateral - similar to median. barely blurs the img
bilateral = cv.bilateralFilter(img, 30, 35, 25)
cv.imshow("bilateral", bilateral)







cv.waitKey(0)