import cv2 as cv

img=cv.imread('/home/siva/Downloads/opencv-4.x/samples/data/sudoku.png',cv.IMREAD_GRAYSCALE)

while img is not None:
    cv.imshow('Image',img)
    _,binary_threshold=cv.threshold(img,127,255,cv.THRESH_BINARY)
    block_size=11
    c=2
    adaptive_mean=cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C,
                    cv.THRESH_BINARY,block_size,c)
    adaptive_gaussian=cv.adaptiveThreshold(img,255,
                        cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY
                        ,block_size,c)
    cv.imshow('Binary',binary_threshold)
    cv.imshow('Adaptive Mean',adaptive_mean)
    cv.imshow('Adaptive Gaussian',adaptive_gaussian)
    if cv.waitKey(0)==ord('q'):
        cv.destroyAllWindows()
        break
