'''
Created on Jan 30, 2019

@author: Sumit
'''
import face_recognition
import cv2
import numpy as np
from _ast import If


def video():
    cam = face_recognition.load_Camera()
    while(True):
        cam,gray = face_recognition.load_image_Camera(cam)
        #faces = faces=face_recognition.face_cascade(cam, gray)
        face_recognition.show_image_file(gray,'Camera')
        if cv2.waitKey(500) & 0xFF == ord('q'):
            break
    face_recognition.realease_Camera()
    cv2.destroyAllWindows()

def main():
    image=face_recognition.load_image_file('image.JPG')
    
    face_recognition.show_image_file(image,'windows')
    cv2.waitKey(0)
cv2.destroyAllWindows()

def face():
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
    
    img = cv2.imread('face.JPG')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    
    cv2.imshow('img',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    

if __name__ == '__main__':
    face()