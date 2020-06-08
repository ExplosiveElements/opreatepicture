import numpy as np
import cv2 as cv

def  m_10_Smooth_create_img(img, r, c, add):
    # 该函数用于生成指定长宽和指定填充边大小的全零图像

    # 生成扩展图像
    img_s = np.zeros([r + add, c + add],np.uint8)
    half = add // 2
    #将原图复制到扩展图像
    img_s[half + 1 : r + half+1, half + 1 : c + half+1] = img
    return img_s

def m_10_Smooth_process_img(img, r, c, m):
    # 该函数用于用指定大小的均值模板平滑指定图像

    # 新图像，用于赋值平滑后的结果
    img_s = np.zeros([r, c],np.uint8)

    # 逐个像素处理
    for x in range(1 , r):
        for y in range(1 , c):
            #滤波器范围内所有像素点之和
            sum = 0
            for i in range(0 , m):
                for j in range(0 , m):
                    sum = sum + img[x + i , y + j ]
            # 除以系数
            img_s[x, y] = sum / (m * m)

    # 返回新图像
    return img_s


def  m_12_Median_Filter_process_img(img_1, r, c, m):
    # 创建一个填充边图像
    img_1s = m_10_Smooth_create_img(img_1, r, c, m - 1)

    # 创建新图像
    img_2 = np.zeros([r, c],np.uint8)
    # 逐个像素处理
    for x in range(1, r):
        for y in range(1 , c):
            # 将滤波器中的所有像素保存起来，用于求中位数
            arr = np.zeros([1, m*m],np.uint8)
            for i in range(0, m):
                for j in range(0, m):
                    arr[0, (i) * m +j-1] = img_1s[x + i -1, y + j-1 ]
            # 求中位数
            img_2[x, y] = np.median(arr)
    return img_2

def m_13_Sharpening_Laplace(img_1, model):

    r,c = img_1.shape
    nu , m = model.shape
    img_1s = m_10_Smooth_create_img(img_1, r, c, m - 1)
    img_2 = np.zeros([r, c],np.uint8)
    img_3 = np.zeros([r, c], np.uint8)

    for x in range(1, r):
        for y in range(1 , c):
            sum1 = 0
            for i in range(0, m):
                for j in range(0, m):
                    sum1 = sum1 + model[i, j] * img_1s[x + i-1 , y + j-1 ]
            if sum1 <= 0:
                img_2[x, y] = 0
            else:
                img_2[x, y] = sum1

            img_3[x, y] = sum1

    return img_2,img_3

def m_15_Gradient_Enhancement_process(img_1, model_1, model_2):

    r, c = img_1.shape
    nu, m = model_1.shape
    img_1s = m_10_Smooth_create_img(img_1, r, c, m - 1)
    img_2 = np.zeros([r, c],np.uint8)

    for x in range(1, r):
        for y in range(1, c):
            sum_1 = 0
            sum_2 = 0
            for i in range(0, m):
                for j in range(0, m):
                    sum_1 = sum_1 + model_1[i, j] * img_1s[x + i - 1, y + j - 1]
                    sum_2 = sum_2 + model_2[i, j] * img_1s[x + i - 1, y + j - 1]
                img_2[x, y] = abs(sum_1) + abs(sum_2)

    return img_2

if __name__ == '__main__':
    im_1 = cv.imread("8.jpg",0)
    r,c = im_1.shape
    m_s = [3, 5, 9, 15, 35]
    list_1=[im_1]
    # for i in range(5):
    #      img_1s = m_10_Smooth_create_img(im_1, r, c, m_s[i] - 1 )
    #      img_2 = m_10_Smooth_process_img(img_1s, r, c, m_s[i])
    #      list_1.append(img_2)

    # img_1s = m_10_Smooth_create_img(im_1, r, c, 3 - 1)
    # img_2 = m_10_Smooth_process_img(img_1s, r, c, 3)
    # list_1.append(img_2)
    # img_3 = m_12_Median_Filter_process_img(im_1,r,c,3)
    # list_1.append(img_3)

    # model_1 = np.array([[0, 1, 0],[1, -4, 1],[0, 1, 0]])
    # model_2 = np.array([[1, 1, 1],[1, -8, 1],[1, 1, 1]])
    # img_2, img_3 = m_13_Sharpening_Laplace(im_1, model_1)
    # img_6, img_7 = m_13_Sharpening_Laplace(im_1, model_2)
    # img_4 = im_1 - img_2
    # img_5 = im_1 - img_6
    # list_1 = list_1+[img_2,img_3,img_4,img_5,img_6,img_7]

    model_1 = np.array([[-1,-2,-1],[0,0,0],[1,2,1]])
    model_2 = np.array([[-1,0,1],[-2, 0, 2],[-1, 0, 1]])
    img_2 = m_15_Gradient_Enhancement_process(im_1, model_1, model_2)
    list_1.append(img_2)

    cv.namedWindow('input_image', cv.WINDOW_AUTOSIZE)
    cv.imshow('input_image',  np.hstack(list_1))
    cv.waitKey(0)
    cv.destroyAllWindows()
