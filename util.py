import cv2
import numpy as np







def sobel_x(path):
    image = cv2.imread(path)
    image= cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    gradients_sobelx = cv2.Sobel(image, -1, 1, 0)
    cv2.imshow('Sobel X', gradients_sobelx)
    
    cv2.waitKey()
    


def sobel_y(path):
    image = cv2.imread(path)
    image= cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gradients_sobely = cv2.Sobel(image, -1, 0, 1)
    cv2.imshow('Sobel Y', gradients_sobely)
    
    cv2.waitKey()

    


def soble_xy(path):
    image = cv2.imread(path)
    image= cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gradients_sobelx = cv2.Sobel(image, -1, 1, 0)
    gradients_sobely = cv2.Sobel(image, -1, 0, 1)

    gradients_sobelxy = cv2.addWeighted(gradients_sobelx, 0.5, gradients_sobely, 0.5, 0)
    cv2.imshow('Sobel X+Y', gradients_sobelxy)
    
    cv2.waitKey()



    


def laplacian(path):
    image = cv2.imread(path)
    image= cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gradients_laplacian = cv2.Laplacian(image, -1)
    cv2.imshow('laplacian', gradients_laplacian)
    
    cv2.waitKey()

    


def canny(path):
    image = cv2.imread(path)
    image= cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    canny_output = cv2.Canny(image, 80, 150)
    cv2.imshow('Canny', canny_output)   
    
    cv2.waitKey()
    


canny('test.jfif')