import numpy as np
import cv2 as cv

image=np.zeros((512,512,3),np.uint8)

def on_blue_change(x):
    image[:,:,0]=x
    cv.imshow('window',image)

def on_green_change(x):
    image[:,:,1]=x
    cv.imshow('window',image)
    
def on_red_change(x):
    image[:,:,2]=x
    cv.imshow('window',image)
    
cv.namedWindow('window')
cv.createTrackbar('blue','window',0,255,on_blue_change)
cv.createTrackbar('green','window',0,255,on_green_change)
cv.createTrackbar('red','window',0,255,on_red_change)

while True:
    cv.imshow('window',image)
    if cv.waitKey(0)==ord('q'):
        cv.destroyAllWindows()
        break
    