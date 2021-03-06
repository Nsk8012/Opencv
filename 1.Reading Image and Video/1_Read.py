import cv2 as cv

img = cv.imread(
    "C:/Users/Nishanth/Desktop/Code/OpenCV/Resources/Photos/cat.jpg")

cv.imshow('Cat', img)

cv.waitKey(0)
