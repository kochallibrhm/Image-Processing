# -*- coding: utf-8 -* -
"""
Created on Thu Oct 15 15:08:36 2020

@author: kochalilibrahim
"""

import os
import numpy as np
import matplotlib.pyplot as plt


def compare_list_ndarray():
    list1 = [1, "2guygyyuyugy,3", '4', 5, 6]
    list2 = [2, "2asdasdasdasdguygyyuyugy, 3", '1114', 15, 26]

    print(list1 + list2)

    list1 = [1, 2, 3, 4]
    list2 = [1, 2, 3, 4]
    list1 + list2 + [10]
    print(list1 + list2 + [10])

    list3 = np.asarray([1, 2, 3, 4])
    list4 = np.asarray([1, 2, 3, 4])
    print(list3 + list4 + 10)


def get_jpeg_files():
    os.getcwd()
    os.listdir()
    path = os.getcwd()
    path = os.getcwd()
    jpg_files = [f for f in os.listdir(path) if f.endswith('.jpg')]
    return jpg_files


compare_list_ndarray()
jpg_files = get_jpeg_files()
print(jpg_files)

image1 = plt.imread('canakkalebogaz.jpg')
image2 = plt.imread('canakkalebogaz1.jpg')


def display_two_image(im1, im2):

    plt.subplot(1, 2, 1)
    plt.imshow(im1)

    plt.subplot(1, 2, 2)
    plt.imshow(im2 + 30)

    plt.show()


display_two_image(image1, image2)


def rotate(im1):

    m, n, k = im1.shape

    new_image = np.zeros((n, m, k), dtype='uint8')

    for i in range(m):
        for j in range(n):
            temp = image1[i, j]
            new_image[j, i] = temp

    return new_image
