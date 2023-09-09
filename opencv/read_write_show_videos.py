import cv2
cap=cv2.VideoCapture(0)
fourcc=cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter('outputs.avi',fourcc,30,(640,480),isColor=False)
while cap.isOpened():
    ret,frame=cap.read()
    if ret:
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        out.write(gray)
        cv2.imshow('frame',frame)
        if cv2.waitKey(1)==ord('q'):
            break
    else:
        break
cap.release()
out.release()
cv2.destroyAllWindows()