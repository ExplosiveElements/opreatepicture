import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt


# 画直方图
def zhifangtu(image):
    a = [0] * 256  # 创建储存像素数的一维数组
    w = image.shape[0]  # 得到图像宽高
    h = image.shape[1]
    # 计算灰度像素数
    for i in range(w):
        for j in range(h):
            gray = image[i, j]
            a[gray] += 1
    # 以灰度为x轴像素数为y轴画直方图
    y = a
    x = [i for i in range(256)]
    plt.figure()
    plt.title("zhifangtu")
    plt.xlabel("Bins")
    plt.ylabel("Pixels")
    plt.bar(x, y)
    plt.xlim([0, 256])
    plt.xlim([0, 256])
    return a  # 返回灰度像素数


# 将图像均衡化
def junhenghua(a, image):  # 入口参数：灰度像素数和图片
    b = [0] * 256  # 储存个灰度像素占比数据
    c = [0] * 256  # 储存累计分布数据
    w = image.shape[0]
    h = image.shape[1]
    mn = w * h * 1.0
    img = np.zeros([w, h], np.uint8)  # 创建空数组储存均衡化后数据

    # 计算灰度分布密度
    for i in range(len(a)):
        b[i] = a[i] / mn
    # 计算累计直方图数据
    for i in range(len(c)):
        if i == 1:
            c[i] = b[i]
        else:
            c[i] = c[i - 1] + b[i]
            a[i] = int(255 * c[i])
    # 对各灰度值进行均衡化映射
    for i in range(w):
        for j in range(h):
            img[i, j] = a[image[i, j]]

    return img  # 返回均衡化后图像


image = cv.imread("Fig3.15(a)4.jpg", 0)  # 读取灰度图像
cv.imshow("base", image)
a = zhifangtu(image)  # 画原始图像直方图并得到灰度像素数
b = junhenghua(a, image)  # 将图像均衡化
cv.imshow('junhenghua', b)
zhifangtu(b)  # 画均衡化后图像直方图
plt.show()
cv.waitKey(0)
cv.destroyAllWindows()