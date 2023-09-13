import cv2

image=cv2.imread('/home/siva/Downloads/opencv-4.x/samples/data/butterfly.jpg')
image2=cv2.imread('/home/siva/Downloads/opencv-4.x/samples/data/graf1.png')

if image is not None:
    # b,g,r=cv2.split(image)
    # cv2.imshow('image',image)
    # cv2.imshow('image2',image2)
    # cv2.imshow('blue',b)
    # cv2.imshow('green',g)
    # cv2.imshow('red',r)
    # merged=cv2.merge((g,r,b))
    # part=image[103:330,0:220]
    image=cv2.resize(image,(512,512))
    image2=cv2.resize(image2,(512,512))
    added_image=cv2.add(image,image2)
    weighted_image=cv2.addWeighted(image,0.8,image2,0.2,100)
    cv2.imshow('added_image',added_image)
    cv2.imshow('weighted_image',weighted_image)
    if cv2.waitKey(0)==ord('q'):
        cv2.destroyAllWindows()