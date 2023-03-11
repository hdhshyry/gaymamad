import cv2 as cv
import numpy as np
img = cv.imread('img.jpg')
# cv.imshow('window',img)
# cv.waitKey(0)
# cv.destroyAllWindows()
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('window',gray)
# cv.waitKey(0)
# cv.destroyAllWindows()
#-------------------------------------------------------------------------------------------------
# b, g, r = cv.split(img)
# img2 = np.hstack([b, g,r ])
# cv.imshow('window', img2)
M = np.ones(gray.shape, dtype='uint8') * 40
brighter = cv.add(gray, M)
darker = cv.subtract(gray, M)
img2 = np.hstack([ brighter])
img3=np.hstack([darker])
cv.imshow('window', img2)
cv.waitKey(0)
cv.destroyAllWindows()
cv.imshow('window', img3)
cv.waitKey(0)
cv.destroyAllWindows()
ret,img1 = cv.threshold(img2,109,255,cv.THRESH_TOZERO)
cv.imshow('window', img1)
cv.waitKey(0)
cv.destroyAllWindows()
#__________________________________________________________________________________________________________________
def trackbar(x):
    ret, img9 = cv.threshold(img2, x, 255, cv.THRESH_BINARY)
    ret, img8 = cv.threshold(img2, x, 255, cv.THRESH_BINARY_INV)
    mg=np.hstack([img9, img8])
    cv.imshow('window',mg )


trackbar(100)
cv.createTrackbar('threshold', 'window', 100, 255, trackbar)
cv.waitKey(0)
cv.destroyAllWindows()