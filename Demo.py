'''
Created on Jan 30, 2019

@author: Sumit
'''
import face_recognition as fr 

def video():
    camera=fr.camera(1)
    camera.load_Camera()
    while(True):
        img=fr.image(camera.cam)
        img.read_Frame()
        #img.gray_frame()
        print('frame', img.frame)
    #    img_frame.show_Frame("title")
        print('inside loop')
        break    
    
    
    
    
    print('outside loop')
    camera.realease_Camera()
    

if __name__ == '__main__':
    video()