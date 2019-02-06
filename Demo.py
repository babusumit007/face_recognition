'''
Created on Jan 30, 2019

@author: Sumit
'''
import face_recognition as fr
import cv2 

def video():
    camera=fr.camera(0)
    camera.load_Camera()
    #camera.read_frame()
    
    while(True):
        img=fr.image(camera.cam)
        img.read_Frame()
        #img.gray_frame()
        img.face_Detection()
        img.show_Frame("Face Recognition")
        if cv2.waitKey(50) & 0xFF == ord('q'):
            break
    
    camera.realease_Camera()
    

if __name__ == '__main__':
    video()