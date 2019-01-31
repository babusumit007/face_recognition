'''
Created on Jan 30, 2019

@author: Sumit
'''
import cv2
import numpy as np

def load_Camera(cameraID=0):
    '''
    initiate camera 
    :param cameraID: connection of camera default is 0 
    '''
    cam = cv2.VideoCapture(cameraID)
    return cam

def realease_Camera(cam):
    '''
    realease camera 
    :param cam: Camera object 
    '''
    cam.release()
    
    
def load_image_Camera(cam):
    '''
    Read image from camera image from camera and return object 
    :param cam: connection of camera default is 0 
    '''
    _, frame = cam.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    return cam,gray



def load_image_file(file, mode='RGB'):
    '''
    Loads an image file (.jpg, .png, etc) into a numpy array
    :param file: image file name or file object to load
    :param mode: format to convert the image to. Only 'RGB' (8-bit RGB, 3 channels) and 'L' (black and white) are supported.
    :return: image contents as numpy array
    '''
    img = cv2.imread(file)
    return img


def show_image_file(img,title='Window'):
    '''
    Show an image file
    :param title: Window name
    :param img: img object
    :return: NA
    '''
    img = cv2.imshow(title,img)
    
    
def face_Detection(gray):
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    
    #for (x,y,w,h) in faces:
    #    cv2.rectangle(cam,(x,y),(x+w,y+h),(255,0,0),2)
    #    roi_gray = gray[y:y+h, x:x+w]
    #    roi_color = cam[y:y+h, x:x+w]
    return True