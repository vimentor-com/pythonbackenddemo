import cv2
import numpy as np


def show_img(img, winname="TEST"):
    from matplotlib import pyplot
    pyplot.figure()
    pyplot.imshow(img, cmap='gray')
    pyplot.title(winname)
    pyplot.show()


def image_cut(img, num=10):
    small_imgs_dic = list()
    high = img.shape[0]
    smal_high = high // num

    for i in range(num):
        if i < num - 1:
            simage = img[i * smal_high:(i + 1) * smal_high:, :, :]
            small_imgs_dic.append(convert_to_grayscale(simage))
        else:
            simage = img[i * smal_high:, :, ]
            small_imgs_dic.append(convert_to_grayscale(simage))

    return small_imgs_dic


def convert_to_grayscale(image):
    converted_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    return converted_img


def image_merge(images):
    return np.concatenate(images, axis=0)


def process_img(img):
    print('Cut anh goc thanh 3 anh nho hon')
    cut_image = image_cut(img, num=3)
    print('Ghep lai cac anh nho da duoc cat va chuyen mau')
    merged_img = image_merge(cut_image)
    print("Luu anh da chuyen doi vao cung thu muc voi anh goc")
    cv2.imwrite("images/output_sample.jpg", merged_img)
    print("Hoan thanh viec chuyen mau cho anh")


if __name__ == '__main__':
    img = cv2.imread("images/input_sample.jpg")
    process_img(img)

