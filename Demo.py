'''
Created on Jan 30, 2019

@author: Sumit
'''
import face_recognition as fr 

def video():
    camera=fr.camera(0)
    camera.load_Camera()
    #camera.read_frame()
    
    while(True):
        img=fr.image(camera.cam)
        img.read_Frame()
        img.gray_frame()
        img.show_Frame("title")
        break    
    
    camera.realease_Camera()
    

if __name__ == '__main__':
    video()