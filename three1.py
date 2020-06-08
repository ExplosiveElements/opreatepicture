import numpy as np
import cv2 as cv
import math

def image_reverse(input_image):
    rows, cols = input_image.shape
    max1 = input_image.max()

    emptyImage= np.zeros([rows, cols], np.uint8)

    for i in range(rows):
        for j in range(cols):
            emptyImage[i, j] = max1 - input_image[i, j]

    return emptyImage


def image_log(input_image,c):
    rows, cols,= input_image.shape
    emptyImage = np.zeros((rows, cols), np.uint8)
    max1 = input_image.max()
    print(max1)


    for i in range(rows):
        for j in range(cols):
             r = input_image[i, j]
             # 重新量化
             emptyImage[i, j] = ((c * math.log(1 + r) - c * math.log(1 + 0)) /
                                       (c * math.log(1 + max1) - c * math.log(1 + 0))) * max1

    return emptyImage


def imagr_gama(input_image, gamma):
    rows, cols= input_image.shape
    emptyImage = np.zeros((rows, cols), np.uint8)
    max1 = input_image.max()

    for i in range(rows):
        for j in range(cols):
            r = input_image[i, j]

            emptyImage[i, j] =  ((r/max1)**gamma )* max1

    return emptyImage


if __name__ == '__main__':
    image1 = cv.imread("1.jpg", 0)
    image_reverses = image_reverse(image1)
    cv.namedWindow('input_image', cv.WINDOW_AUTOSIZE)
    cv.imshow('input_image',np.hstack([image1, image_reverses]))

    image2 = cv.imread("2.jpg", 0)
    image_logs = image_log(image2,1)
    cv.namedWindow('input_image1', cv.WINDOW_AUTOSIZE)
    cv.imshow('input_image1', np.hstack([image2, image_logs]))

    image3 = cv.imread("3.jpg", 0)
    image_gamas1 = imagr_gama(image3, 0.75)
    cv.namedWindow('input_image2', cv.WINDOW_AUTOSIZE)
    cv.imshow('input_image2', np.hstack([image3, image_gamas1]))

    image4 = cv.imread("4.jpg", 0)
    mage_gamas2 = imagr_gama(image4, 3)
    cv.namedWindow('input_image3', cv.WINDOW_AUTOSIZE)
    cv.imshow('input_image3', np.hstack([image4, mage_gamas2]))

    cv.waitKey(0)
    cv.destroyAllWindows()
