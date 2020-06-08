import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

src = cv.imread('Lena.jpg')
cv.namedWindow('input_image', cv.WINDOW_AUTOSIZE)
cv.imshow('input_image', src)


row, col, channel = src.shape
lenna_gray = np.zeros([row, col], np.uint8)
for r in range(row):
    for l in range(col):
        lenna_gray[r, l] = 1 / 3 * src[r, l, 0] + 1 / 3 * src[r, l, 1] + 1 / 3 * src[r, l, 2]
cv.namedWindow('lenna_gray', cv.WINDOW_AUTOSIZE)
cv.imshow("lenna_gray", lenna_gray)

M = np.zeros([row, col], np.uint8)

for i in range(1,row):
    for j in range(1,col):
        if lenna_gray[i, j] < 175:
            M[i, j] = 0
        else:
            M[i, j] = 255
cv.namedWindow('M', cv.WINDOW_AUTOSIZE)
cv.imshow("M", M)

a = [0] * 256  # 创建储存像素数的一维数组
w = lenna_gray.shape[0]  # 得到图像宽高
h = lenna_gray.shape[1]
# 计算灰度像素数
for i in range(w):
    for j in range(h):
        gray = lenna_gray[i, j]
        a[gray] += 1
# 以灰度为x轴像素数为y轴画直方图
y = a
x = [i for i in range(256)]
plt.figure()
plt.title("zhifangtu")
plt.xlabel("Bins")
plt.ylabel("Pixels")
plt.bar(x, y)
plt.show()
print(col*row)
cv.waitKey(0)
cv.destroyAllWindows()
cv.imwrite("gray.jpg",lenna_gray)
cv.imwrite("erzhi1.jpg", M)