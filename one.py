import cv2 as cv
import numpy as np

src = cv.imread('Lena.jpg')
cv.namedWindow('input_image', cv.WINDOW_AUTOSIZE)
cv.imshow('input_image', src)
cv.waitKey(0)
cv.destroyAllWindows()