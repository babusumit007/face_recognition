'''
Created on Feb 6, 2019

@author: Sumit
'''
import os
import pickle
from PIL import Image
import numpy as np
import cv2

BASE_DIR = os.path.dirname(os.path.abspath(__name__))

face_cascade = cv2.CascadeClassifier('.//face_recognition//Tools//haarcascade_frontalface_default.xml')

y_lables = []
x_train = []

def create(images):
    image_dir = os.path.join(BASE_DIR, images)
    for root, dirs, files in os.walk(image_dir):
        for file in files:
            if file.endswith("png") or ("jpg"):
                path = os.path.join(root, file)
                lable = os.path.basename(root).replace(" ","-" ).lower()
                #print(lable, path)
                #y_lables.append(lable)
                #x_train.append(path)
                pil_image = Image.open(path).convert("L")#grayscale
                image_array = np.array(pil_image)
                #print(image_array)
                faces = face_cascade.detectMultiScale(image_array, scaleFactor=1.55, minNeighbors=5, minSize=(40,40))
                for (x,y,w,h) in faces:
                    cv2.rectangle(image_array,(x,y),(x+w,y+h),(255,0,0),2)
                    roi_color = image_array[y:y+h, x:x+w]
                    print(roi_color)
                    x_train.append(roi_color)
                    
                    
                    
                    
                    
                    #while True:
                    #    cv2.imshow('temp',image_array)
                    #    if cv2.waitKey(50) & 0xFF == ord('q'):
                    #        break
 
                
#print(x_train)                