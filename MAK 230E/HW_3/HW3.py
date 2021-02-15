#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 12:13:18 2021

@author: Baran Berk Bağcı
"""

"""
READ ME !!!!

This py file use OpenCV library for Image Processing therefore if you want to run this program you must install OpenCV on
python 3.6.10 on Anaconda root (base) environmant. Python 3.6.10 since OpenCV only run in this version. And also numpy and matplotlib must be
installed. All the picture are inside the img folder so if you want to run this program you must create folder named img and put all of the images inside that folder or
delete "img/" path from capture objects and put images same folder with this program. 
"""

import cv2 #import OpenCV
import numpy as np #import numpy library
import matplotlib.pyplot as plt  #import matplotlib
 

"""
Chromium alloy part (chromium_alloy.gif)
For this task we try to find borders of alloy
"""

gif = cv2.VideoCapture("img/chromium alloy.gif")  #capture inside the img folder chromium alloy gif


ret, img = gif.read() # read gif and there is a gif object
if ret != False: #if statement check ret object if it did not exist opencv cant show or process captured object
    canny = cv2.Canny(img,100,200) # canny method is used for detecting dark edges 100 and 200 parameters I find them by experimenting myself for further detail please look this link: https://docs.opencv.org/master/da/d22/tutorial_py_canny.html
   
    cv2.imshow('Canny Video', canny) # this imshow method stream the processed canny image
    
    cv2.waitKey(4000) # This is delay function show gif for 4000 ms(milisecond). 


        

"""
George Clooney part (800.png)

This part we try to sharpen the image however when image is blurred lots of data lost so we cannot make original image without using deep learning.

This we make hard coding to make possible way to save image for blurrying

"""


im = cv2.imread("img/800.jpg") #capture/read inside the img folder 800.jpg (George Cooleny).
blur_matrix = np.ones((5,5),np.float32)/25 # making blurring matrix
sharp_matrix = np.array([[-1,-1, -1], [-1, 9, -1], [-1,-1, -1]]) #This matrix sharped matrix which is used for filtering.



for  i in range(4): # for loop sharpened image 4 times 
  for j in range(3): # for loop blur image for 3 times
    dst = cv2.filter2D(im,-1,blur_matrix) #blur the image
  im = cv2.filter2D(dst, -1, sharp_matrix) #this method used for filterin image by identified matrix





cv2.imshow("Sharpened Photo", im) #OpenCV show SHarpened Image
    
cv2.waitKey(1000) # Delay function show picture for 1000 ms (milisecond).



"""
Pipes part (pipes.png)

For this task we try to cont and draw circle borders on pipe image

image coloring part

"""


img = cv2.imread("img/pipes.jpg") # capture/read inside the img folder pipes.jpg
horizontal_blur = cv2.filter2D(img[:, :, 0], cv2.CV_32F, kernel=np.ones((11,1,1), np.float32)/11.0, borderType=cv2.BORDER_CONSTANT) #this fiter turn image to 32bit format and multiply kernels by 11,1,1 dimensinal with all variables 1/11.0 matrix which is standart matrix for this image and blur horizantal edges
vertical_blur = cv2.filter2D(img[:, :, 0], cv2.CV_32F, kernel=np.ones((1,11,1), np.float32)/11.0, borderType=cv2.BORDER_CONSTANT) #this fiter turn image to 32bit format and multiply kernels by 1,11,1 dimensinal with all variables 1/11.0 matrix which is standart matrix for this image and blur vertical edges
mask = ((img[:,:,0]>horizontal_blur*1.2) | (img[:,:,0]>vertical_blur*1.2)).astype(np.uint8)*255 # this is masking blurred image, turn them 8bit format and help to find radial edges

"""
Pipes part (pipes.png)

circle counting part

"""

image = cv2.imread("img/pipes.jpg") # capture/read inside the img folder pipes.jpg
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #gray filter image because rgb images include more uneccesary data
thresh = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV,27,3) #threshold the image

centers = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) #find countours
centers = centers[0] if len(centers) == 2 else centers[1] #find circle centers
count = 0 # count variable = 0
for c in centers: # for loop to count circles
    area = cv2.contourArea(c) # circle areas
    x,y,w,h = cv2.boundingRect(c) # find bound rectangle
    ratio = w/h # ratio
    ((x, y), r) = cv2.minEnclosingCircle(c)
    if ratio > .10 and ratio < 5.20 and area > 27 and area < 120 and r < 700: # if statements for counting circles
        cv2.circle(image, (int(x), int(y)), int(r), (36, 255, 12), -1)
        count += 1 # circle count variable


cv2.imshow("Pipes", mask) #show processed pipe image
print("Circle count is: {}".format(count)) #print counted circle count variables
cv2.waitKey(0) # this method is delay howerver, when it got 0 by its parameters it is show image untill any button pressed on keyboard


cv2.destroyAllWindows() #kill all windows


