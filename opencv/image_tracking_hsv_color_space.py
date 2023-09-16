import cv2 as cv
import numpy as np

cap=cv.VideoCapture(0)
fourcc=cv.VideoWriter_fourcc(*'XVID')
out=cv.VideoWriter('imamge_tracking.avi',fourcc,30,(640,480))

while cap.isOpened():
    ret,frame=cap.read()
    if ret:
        hsv=cv.cvtColor(frame,cv.COLOR_BGR2HSV)
        l_b=np.array([94,112,83])
        u_b=np.array([156,255,255])
        mask=cv.inRange(hsv,l_b,u_b)
        res=cv.bitwise_and(frame,frame,mask=mask)
        cv.imshow('output',res)
        out.write(res)
        if cv.waitKey(1)==ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv.destroyAllWindows()