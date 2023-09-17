import cv2 as cv

img=cv.imread('/home/siva/Downloads/opencv-4.x/samples/data/gradient.png')

while img is not None:
    _,binary_threshold=cv.threshold(img,127,255,cv.THRESH_BINARY)
    _,inverse_binary_threshold=cv.threshold(img,127,255,cv.THRESH_BINARY_INV)
    _,truncated_threshold=cv.threshold(img,127,255,cv.THRESH_TRUNC)
    _,to_zero_threshold=cv.threshold(img,127,255,cv.THRESH_TOZERO)
    _,to_zero_inverse=cv.threshold(img,127,255,cv.THRESH_TOZERO_INV)
    # cv.imshow('Binary threshold',binary_threshold)
    # cv.imshow('Inverse Binary threshold',inverse_binary_threshold)
    # cv.imshow('Truncated threshold',truncated_threshold)
    # cv.imshow('To zero threshold',to_zero_threshold)
    cv.imshow('To zero inverse',to_zero_inverse)
    cv.imshow('Image',img)
    if cv.waitKey(0)==ord('q'):
        cv.destroyAllWindows()
        break