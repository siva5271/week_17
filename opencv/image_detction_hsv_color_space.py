import cv2 as cv
import numpy as np

def nothing(x):
   pass

cv.namedWindow('tracking')
cv.createTrackbar('LH','tracking',0,255,nothing)
cv.createTrackbar('LS','tracking',0,255,nothing)
cv.createTrackbar('LV','tracking',0,255,nothing)
cv.createTrackbar('UH','tracking',255,255,nothing)
cv.createTrackbar('US','tracking',255,255,nothing)
cv.createTrackbar('UV','tracking',255,255,nothing)



while True:
    image=cv.imread('/home/siva/Downloads/opencv-4.x/samples/data/smarties.png')
    hsv=cv.cvtColor(image,cv.COLOR_BGR2HSV)
    l_h=cv.getTrackbarPos('LH','tracking')
    l_s=cv.getTrackbarPos('LS','tracking')
    l_v=cv.getTrackbarPos('LV','tracking')
    u_h=cv.getTrackbarPos('UH','tracking')
    u_s=cv.getTrackbarPos('US','tracking')
    u_v=cv.getTrackbarPos('UV','tracking')
    
    l_b=np.array([l_h,l_s,l_v])
    u_b=np.array([u_h,u_s,u_v])
    
    mask=cv.inRange(hsv,l_b,u_b)
    res=cv.bitwise_and(image,image,mask=mask)
    #res_converted=cv.cvtColor(res,cv.COLOR_HSV2BGR)
    cv.imshow('Image',image)
    cv.imshow('Mask',mask)
    cv.imshow('Result',res)
    # cv.imshow('tracking',image)
    if cv.waitKey(1)==ord('q'):
        break
cv.destroyAllWindows()
#blue->lb->[94,112,83]
#blue->ub->[156,255,255]
#red->lb->[0,230,150]
#red->ub->[10,255,242]
#green->lb->[64,47,176]
#green->ub->[84,255,255]