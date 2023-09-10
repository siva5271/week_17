import cv2
import numpy as np
total_points=[]
def mouse_event(event,x,y,frames,params):
    if event==cv2.EVENT_LBUTTONDOWN:
        total_points.append((x,y))
        if len(total_points)>1:
            cv2.arrowedLine(image,total_points[-2],total_points[-1],[0,0,255],3)
        else:
            cv2.circle(image,(x,y),3,[0,0,255],1)
        cv2.imshow('image',image)

image=np.ones([512,512,3],dtype=np.uint8)*255
if image is not None:
    cv2.imshow('image',image)
    cv2.setMouseCallback('image',mouse_event)
    if cv2.waitKey(0)==ord('q'):
        cv2.destroyAllWindows()
