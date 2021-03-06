import cv2 as cv

img = cv.imread(
    "C:/Users/Nishanth/Desktop/Code/OpenCV/Resources/Photos/cat_large.jpg")

cv.imshow('Cat Large', img)

cv.waitKey(0)
