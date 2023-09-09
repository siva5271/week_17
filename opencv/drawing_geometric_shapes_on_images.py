import cv2
import numpy as np

image=cv2.imread('images/satellite_view.jpg')
# image=np.ones((640,480,3),dtype=np.uint8)*255
if image is not None:
    tip_length=0.1
    color=(0,0,255)
    thickness=5
    cv2.line(image,(100,300),(300,300),color,thickness)
    cv2.arrowedLine(image,(300,100),(300,300),color,thickness)
    cv2.rectangle(image,(50,50),(350,350),color,thickness)
    cv2.circle(image,(200,200),150,color,thickness)
    cv2.putText(image,"open_cv",(200,200),cv2.FONT_HERSHEY_SIMPLEX,1,color,3)
    cv2.imshow('image',image)
    
if cv2.waitKey(0)==ord('q'):    
    cv2.destroyAllWindows()