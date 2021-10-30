import cv2 as cv

img = cv.imread('../photos/trck-pic-1.jpg')

cv.imshow('img', img)

#grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

#Blur
blur_img = cv.GaussianBlur(img, (3, 3), cv.BORDER_DEFAULT)
cv.imshow('blur', blur_img)

#Edge Cascade
canny = cv.Canny(blur_img, 125, 175)
cv.imshow('canny', canny)

#dilation
dilate = cv.dilate(canny, (11,11), iterations=3)
cv.imshow('dilate', dilate)

#erode
eroded = cv.erode(dilate, (3,3), iterations=1)
cv.imshow('eroded', eroded)

#resize

resized = cv.resize(dilate, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('resized', resized)

#cropping
cropped = dilate[50:200, 200:400]
cv.imshow('crop', cropped)





cv.waitKey(0)