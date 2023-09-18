import matplotlib.pyplot as plt
import cv2 as cv

img=cv.imread('/home/siva/Downloads/opencv-4.x/samples/data/apple.jpg')
img=cv.cvtColor(img,cv.COLOR_BGR2RGB)

plt.imshow(img)
plt.show()
