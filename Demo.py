'''
Created on Jan 30, 2019

@author: Sumit
'''
import face_recognition
import cv2
import numpy as np


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
    pass
    

if __name__ == '__main__':
    face()