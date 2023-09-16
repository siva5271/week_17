import cv2 as cv
import numpy as np

cap=cv.VideoCapture(0)
fourcc=cv.VideoWriter_fourcc(*'XVID')
out=cv.VideoWriter('outputs.avi',fourcc,30,(640,480))