'''
Created on Jan 30, 2019

@author: Sumit
'''
import face_recognition as fr
import cv2 
import face_recognition.faces_train as ft


def video():
    camera=fr.camera(0)
    camera.load_Camera()
    labels=ft.read()
    #camera.read_frame()
    
    while(True):
        img=fr.image(camera.cam)
        img.read_Frame()
        img.gray_frame()
        img.face_Detection(labels)
        #img.write_image("sumit")
        img.show_Frame("Face Recognition")
        if cv2.waitKey(50) & 0xFF == ord('q'):
            break
    
    camera.realease_Camera()
    

if __name__ == '__main__':
    video()
    #ft.create("images")