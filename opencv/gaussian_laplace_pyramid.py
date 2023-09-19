import cv2 as cv
import numpy as np

image=cv.imread('/home/siva/Downloads/opencv-4.x/samples/data/baboon.jpg')

gaussian=[image]

for i in range(5):
    temp_image=cv.pyrDown(gaussian[i])
    gaussian.append(temp_image)

for i in range(len(gaussian)):
    title='Gaussian'+str(i)
    cv.imshow(title,gaussian[i])
    
laplace=[]

for i in range(len(gaussian)-1,0,-1):
    expanded=cv.pyrUp(gaussian[i])
    temp_image=cv.subtract(gaussian[i-1],expanded)
    laplace.append(temp_image)

for i in range(len(laplace)):
    title='Laplace'+str(i+1)
    cv.imshow(title,laplace[i])

if cv.waitKey(0)==ord('q'):
    cv.destroyAllWindows()