#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import cv2 as cv


def nothing(x):
    pass




cimg  = cv.imread('img/priz.png',0)
#img = cv.imread('img/priz.png', cv.IMREAD_GRAYSCALE)
cimg = cv.medianBlur(cimg,5)
#cimg = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.namedWindow('Trackbars')

cv.resizeWindow('Trackbars',640,240)

#cv.createTrackbar('circle', 'Trackbars',0,255,nothing)
#cv.createTrackbar('param 1','Trackbars',0,255,nothing)
#cv.createTrackbar('param 2','Trackbars',0,255,nothing)
#cv.createTrackbar('min Radius','Trackbars',0,100,nothing)
#cv.createTrackbar('max Radius','Trackbars',0,100,nothing)
cv.createTrackbar('X1', 'Trackbars',-1000,1000,nothing)
cv.createTrackbar('Y1', 'Trackbars',-1000,1000,nothing)
cv.createTrackbar('X2', 'Trackbars',-1000,1000,nothing)
cv.createTrackbar('Y2', 'Trackbars',-1000,1000,nothing)

while True:
    
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        cv.destroyAllWindows()
        break
    
    x1 = cv.getTrackbarPos('X1', 'Trackbars')
    y1 = cv.getTrackbarPos('Y1', 'Trackbars')
    x2 = cv.getTrackbarPos('X2', 'Trackbars')
    y2 = cv.getTrackbarPos('Y2', 'Trackbars')
    #circle = cv.getTrackbarPos('circle','Trackbars')    
    #para1 = cv.getTrackbarPos('param 1','Trackbars')
    #para2 = cv.getTrackbarPos('param 2','Trackbars')
    #minRadiu = cv.getTrackbarPos('min Radius','Trackbars')
    #maxRadiu = cv.getTrackbarPos('max Radius','Trackbars')

    circles = cv.HoughCircles(cimg,cv.HOUGH_GRADIENT,1,14, param1 = 50, param2 = 132, minRadius = 0, maxRadius = 0)
    circles = np.uint16(np.around(circles))

    #print(circles[0,:]) ((i[0] - 10/2), (i[1] - 10/2)), ((i[0] + 10/2), (i[1] + 10/2))

    for i in circles[0,:]:
        img = cimg.copy()
        img = cv.cvtColor(cimg,cv.COLOR_GRAY2RGB)
        # draw the outer circle
        cv.circle(img,(i[0],i[1]),i[2],(0,255,0),2)
        # draw the center of the circle
        cv.circle(img,(i[0],i[1]),2,(0,0,255),3)
        cv.putText(img, 'Plug', (i[0] - x2, i[1] - (529+y2)), cv.FONT_HERSHEY_SIMPLEX, 
                   1, (255,255,255), 2, cv.LINE_AA)
        cv.rectangle(img,(i[0] + 536, i[1] + 457), (i[0] - 541, i[1] - 529),(0,255,0),3)
        #print(i[0],i[1])
        cv.imshow('Plug',img)

    cimg  = cv.imread('img/priz.png',0)
    cimg = cv.medianBlur(cimg,5)
    #cimg = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    cv.namedWindow('Trackbars')