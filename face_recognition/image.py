'''
Created on Jan 30, 2019

@author: Sumit
'''
import cv2
import numpy as np



def load_image_file(file, mode='RGB'):
    """
    Loads an image file (.jpg, .png, etc) into a numpy array
    :param file: image file name or file object to load
    :param mode: format to convert the image to. Only 'RGB' (8-bit RGB, 3 channels) and 'L' (black and white) are supported.
    :return: image contents as numpy array
    """
    img = cv2.imread(file,0)
    return img


def show_image_file(img,title='Window'):
    """
    Show an image file
    :param title: Window name
    :param img: img object
    :return: NA
    """
    img = cv2.imshow(title,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()