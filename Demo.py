'''
Created on Jan 30, 2019

@author: Sumit
'''
import face_recognition

def main():
    image=face_recognition.load_image_file('image.JPG')
    face_recognition.show_image_file(image)

if __name__ == '__main__':
    main()