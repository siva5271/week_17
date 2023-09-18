import cv2 as cv
import matplotlib.pylab as plt

img=cv.imread('/home/siva/Downloads/opencv-4.x/samples/data/gradient.png')
img=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

_,binary_threshold=cv.threshold(img,127,255,cv.THRESH_BINARY)
_,inverse_binary_threshold=cv.threshold(img,127,255,cv.THRESH_BINARY_INV)
_,truncated_threshold=cv.threshold(img,127,255,cv.THRESH_TRUNC)
_,to_zero_threshold=cv.threshold(img,127,255,cv.THRESH_TOZERO)
_,to_zero_inverse=cv.threshold(img,127,255,cv.THRESH_TOZERO_INV)
    # cv.imshow('Binary threshold',binary_threshold)
    # cv.imshow('Inverse Binary threshold',inverse_binary_threshold)
    # cv.imshow('Truncated threshold',truncated_threshold)
    # cv.imshow('To zero threshold',to_zero_threshold)
    # cv.imshow('To zero inverse',to_zero_inverse)
    # cv.imshow('Image',img)
titles=['Binary threshold','Inverse Binary threshold',
        'Truncated threshold','To zero threshold',
        'To zero inverse','Image']
images=[binary_threshold,inverse_binary_threshold,
        truncated_threshold,to_zero_threshold,to_zero_inverse,
        img]
for i in range(6):
    plt.subplot(2,3,i+1)
    plt.imshow(images[i],'gray',aspect='equal')
    plt.title(titles[i])
    # if cv.waitKey(0)==ord('q'):
    #     cv.destroyAllWindows()
    #     break

plt.tight_layout()
plt.show()