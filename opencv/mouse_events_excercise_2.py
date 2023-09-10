import cv2
import numpy as np

image=cv2.imread('/home/siva/Downloads/opencv-4.x/samples/data/baboon.jpg')

def mouse_event(event,x,y,frames,params):
    if event==cv2.EVENT_LBUTTONDOWN:
        background=np.ones([512,512,3],dtype=np.uint8)*[image[y,x,0],image[y,x,1],image[y,x,2]]
        cv2.imshow('Color Picker',background)
        if cv2.waitKey(0)==ord('p'):
            cv2.destroyWindow('Color Picker')

if image is not None:
    cv2.imshow('Image',image)
    cv2.setMouseCallback('Image',mouse_event)
    if cv2.waitKey(0)==ord('q'):
        cv2.destroyAllWindows()
