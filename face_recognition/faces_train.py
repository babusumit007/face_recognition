'''
Created on Feb 6, 2019

@author: Sumit
'''
import os

BASE_DIR = os.path.dirname(os.path.abspath(__name__))

def create(images):
    image_dir = os.path.join(BASE_DIR, images)
    for root, dirs, files in os.walk(image_dir):
        for file in files:
            if file.endswith("png") or ("jpg"):
                path = os.path.join(root, file)
                lable = os.path.basename(root).replace(" ","-" ).lower()
                print(lable, path)