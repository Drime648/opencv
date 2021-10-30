import cv2 as cv
import numpy as np

img = cv.imread('../photos/trck-pic-1.jpg')

cv.imshow('img', img)

#Translation
def translate(img, x, y):
    transMatrix = np.float32([
        [1, 0, x],
        [0, 1, y]
    ])

    dims = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMatrix, dims)

# x positive is right
# y positive is down
trans = translate(img, 50, 50)





cv.imshow('trans', trans)

cv.waitKey(0)