import cv2 as cv
import numpy as np

img=cv.imread('/home/siva/Downloads/opencv-4.x/samples/data/butterfly.jpg')
kernel=[3,3]
blurred_image=cv.blur(img,kernel)

while img is not None:
    cv.imshow('Source',img)
    cv.imshow('2D convolution',blurred_image)
    if cv.waitKey(0)==ord('q'):
        cv.destroyAllWindows()
        break
