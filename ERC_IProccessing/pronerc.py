#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np 
import cv2 as cv

def nothing(x):
    pass

cimg  = cv.imread('img/probalt.png',0)
cimg = cv.medianBlur(cimg,5)
#cimg = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.namedWindow('detected circles')

cv.resizeWindow('detected circles',640,240)

cv.createTrackbar('circle', 'detected circles',0,255,nothing)
#cv.createTrackbar('param 1','detected circles',0,255,nothing)
cv.createTrackbar('param 2','detected circles',0,255,nothing)
#cv.createTrackbar('min Radius','detected circles',0,100,nothing)
#cv.createTrackbar('max Radius','detected circles',0,100,nothing)

while True:
    
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        cv.destroyAllWindows()
        break
    
    circle = cv.getTrackbarPos('circle','detected circles')    
    #para1 = cv.getTrackbarPos('param 1','detected circles')
    para2 = cv.getTrackbarPos('param 2','detected circles')
    #minRadiu = cv.getTrackbarPos('min Radius','detected circles')
    #maxRadiu = cv.getTrackbarPos('max Radius','detected circles')

    circles = cv.HoughCircles(cimg,cv.HOUGH_GRADIENT,1,140, param1 = 50, param2 = 200, minRadius = 0, maxRadius = 0)
    circles = np.uint16(np.around(circles))

    

    for i in circles[0,:]:
        
        # draw the outer circle
        cv.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
        # draw the center of the circle
        cv.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
        cv.putText(cimg, 'Circle', (i[0],i[1]), cv.FONT_HERSHEY_SIMPLEX, 
                   1, (255,0,0), 2, cv.LINE_AA)
        cv.imshow('Circle',cimg)

    cimg  = cv.imread('img/probalt.png',0)
    cimg = cv.medianBlur(cimg,5)
    #cimg = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    cv.namedWindow('detected circles')
        
 