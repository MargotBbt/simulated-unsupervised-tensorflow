import numpy as np
import os
import cv2
from PIL import Image 
import scipy.misc

def load_images_from_folder(folder):
    images = []
    images_originales = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        img_origin = cv2.imread(os.path.join(folder,filename))
        grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        if img is not None:
            images.append(grey_img)
            images_originales.append(img_origin)
    return images, images_originales

images, images_originales = load_images_from_folder('hand/Synthetic_Images')
for i in range(len(images)):
    name = 'hand/Synthetic_Images/{}_cropped.png'.format(i+1)
    cv2.imwrite(name, images[i])

for i in range(len(images_originales)):
    name = 'hand/Synthetic_Images/{}.jpg'.format(i+1)
    cv2.imwrite(name, images_originales[i])
