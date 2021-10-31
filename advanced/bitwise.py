import cv2 as cv
import numpy as np

blank = np.zeros((400, 400), dtype = np.uint8)


rectangle = cv.rectangle(blank.copy(), (30,30),(370,370), 255, -1)

circle = cv.circle(blank.copy(), (200, 200), 200, 255, -1)

cv.imshow('rectangle', rectangle)
cv.imshow('circle', circle)

#bitwise AND:puts 2 images on top of each other,
#  returns the intersection of two images

bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow("bitwise and", bitwise_and)


#bitwise or: returns intersecting + non intersecting parts
#basically just puts both images on top of each other.
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow("bitwise or", bitwise_or)


#bitwise xor: puts them on each other, and returns
#non intersecting regions

bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow("xor", bitwise_xor)
#bitwise or - bitwise and = bitwise xor


#bitwise not: inverts binary color
#it converts white to black, and white to black.

bitwise_not = cv.bitwise_not(circle)
cv.imshow("circle-not", bitwise_not)


cv.waitKey(0)