'''
Created on Feb 6, 2019

@author: Sumit
'''
import os
import pickle
from PIL import Image
import numpy as np
import cv2
import pickle

BASE_DIR = os.path.dirname(os.path.abspath(__name__))

face_cascade = cv2.CascadeClassifier('.//face_recognition//Tools//haarcascade_frontalface_default.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()


def create(images):
    current_id=0
    lables_ids={}
    y_lables = []
    x_train = []

    image_dir = os.path.join(BASE_DIR, images)
    for root, dirs, files in os.walk(image_dir):
        for file in files:
            if file.endswith("png") or ("jpg"):
                path = os.path.join(root, file)
                lable = os.path.basename(root).replace(" ","-" ).lower()
                #print(lable, path)
                if not lable in lables_ids:
                    lables_ids[lable] = current_id
                    current_id += 1
                id_ = lables_ids[lable]
                pil_image = Image.open(path).convert("L")#grayscale
                image_array = np.array(pil_image)
                #print(image_array)
                faces = face_cascade.detectMultiScale(image_array, scaleFactor=1.55, minNeighbors=5, minSize=(40,40))
                
                
                for (x,y,w,h) in faces:
                    roi = image_array[y:y+h, x:x+w]
                    x_train.append(roi)
                    y_lables.append(id_)
                    print(x_train, y_lables )
                    
    with open('labels.pickle', 'wb') as f:
        pickle.dump(lables_ids,f)  
        
    recognizer.train(x_train,np.array(y_lables))   
    recognizer.save("trainner.yml")     