import cv2
#if the user presses escape, the window is closed
#if 's' is pressed, then the image is saved
image=cv2.imread('/home/siva/Downloads/opencv-4.x/samples/data/aero1.jpg',0)
cv2.imshow('image',image)
k=cv2.waitKey(0)
if k==27:
    cv2.destroyAllWindows()
elif k==ord('s'):
    cv2.imwrite('images/satellite_view.jpg',image)
    cv2.destroyAllWindows()
