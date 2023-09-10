import cv2
import numpy

def mouse_callback(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        display_text=str(x)+', '+str(y)
        fontFace=cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(image,display_text,(x,y),fontFace,1,(0,255,255),3)
        cv2.imshow('image',image)
    if event==cv2.EVENT_RBUTTONDOWN:
        display_text=str(image[y,x][0])+', '+str(image[y,x][1])+', '+str(image[y,x][2])
        fontFace=cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(image,display_text,(x,y),fontFace,1,(255,0,255),3)
        cv2.imshow('image',image)
        
image=cv2.imread('/home/siva/Downloads/opencv-4.x/samples/data/aloeGT.png')
if image is not None:
    cv2.imshow('image',image)
    cv2.setMouseCallback('image',mouse_callback)
    if cv2.waitKey(0)==ord('q'):
        cv2.destroyAllWindows()
else:
    print('Image not found')
    
