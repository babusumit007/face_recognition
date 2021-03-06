'''
Created on Jan 30, 2019

@author: Sumit
'''
import os
import cv2
from _elementtree import Element
import pickle

class camera(Element):
    def __init__(self, cameraID):
        self.camera=cameraID
        self.cam=None

    def load_Camera(self):
        '''
        initiate camera 
        :param NA 
        '''
        self.cam = cv2.VideoCapture(self.camera)
    
    def read_frame(self):
        '''
        initiate camera 
        :param NA 
        '''
        _, frame = self.cam.read()
        return frame
    
    def realease_Camera(self):
        '''
        realease camera 
        :param NA 
        '''
        self.cam.release()


class image(Element):
    def __init__(self, cam):
        self.frame=None
        self.cam = cam
        self.gray=None
        self.face_cascade = cv2.CascadeClassifier('.//face_recognition//Tools//haarcascade_frontalface_default.xml')
        
        self.recognizer = cv2.face.LBPHFaceRecognizer_create()
        self.recognizer.read("trainner.yml")
        
        
        
    def read_Frame(self):
        '''
        Read image from camera image from camera and return object 
        :param cam: connection of camera default is 0 
        '''
        _, self.frame = self.cam.read()

    
    def gray_frame(self):
        '''
        Read image from camera image from camera and return object 
        :param cam: connection of camera default is 0 
        '''
        self.gray = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)
    
    
    
    def read_image(self, file):
        '''
        Loads an image file (.jpg, .png, etc) into a numpy array
        :param file: image file name or file object to load
        :param mode: format to convert the image to. Only 'RGB' (8-bit RGB, 3 channels) and 'L' (black and white) are supported.
        :return: image contents as numpy array
        '''
        self.frame = cv2.imread(file)
    
    def write_image(self, file_name):
        print(file_name + ".jpg")
        cv2.imwrite(file_name + ".jpg", self.frame)
        
        
    def show_Frame(self, title='Window'):
        '''
        Show an image file
        :param title: Window name
        :param img: img object
        :return: NA
        '''
        img = cv2.imshow(title, self.frame)
    
    def face_Detection(self, labels):
        faces = self.face_cascade.detectMultiScale(self.frame, scaleFactor=1.55, minNeighbors=5, minSize=(40,40))
        #print(labels)
        for (x,y,w,h) in faces:
            
            #roi_color = self.frame[y:y+h, x:x+w]
            roi_gray = self.gray[y:y+h, x:x+w]
            
        
            
            id_,conf=self.recognizer.predict(roi_gray)
            print(conf)
            if conf >=45 and conf<=85:
                print(id_)
                print(labels[id_])
                font = cv2.FONT_HERSHEY_SIMPLEX
                name=labels[id_]
                color=(255,255,255)
                stroke=2
                cv2.putText(self.frame,name, (x,y),font,1, color, stroke, cv2.LINE_AA)
                
            
            
            
            cv2.rectangle(self.frame,(x,y),(x+w,y+h),(255,0,0),2)
        
        
        
        
        
        
        
        
        