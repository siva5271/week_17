import cv2
import numpy as np

image=np.ones((512,512),dtype=np.uint8)*255
# image1=np.zeros_like(image)
# image1[:256][:256]=[255,255,255]
# image2=np.zeros_like(image)
# image2[128:384][0:64]=[255,255,255]
# cv2.imshow('image',image)
cv2.imshow('image',image)
# cv2.imshow('image2',image2)
# bitwise_and=cv2.bitwise_and(image1,image2)
# bitwise_or=cv2.bitwise_or(image1,image2)
# bitwise_xor=cv2.bitwise_xor(image1,image2)
bitwise_not=cv2.bitwise_not(image)
# cv2.imshow('bitwise_and',bitwise_and)
# cv2.imshow('bitwise_or',bitwise_or)
# cv2.imshow('bitwise_xor',bitwise_xor)
cv2.imshow('bitwise_not',bitwise_not)
if cv2.waitKey(0)==ord('q'):
    cv2.destroyAllWindows()
    