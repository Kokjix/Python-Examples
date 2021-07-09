#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2 as cv
import numpy as np
import math

def nothing(x):
    pass

def detection(image):
        
    can = cv.getTrackbarPos('Canny','Trackbars')
    can2 = cv.getTrackbarPos('Canny2','Trackbars')
    a = cv.getTrackbarPos('Approx','Trackbars')
    
        
    original = image.copy()
    #green_m = color_detection(image, lis)
    
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    #blur = cv.medianBlur(gray,5)
    thresh =  cv.Canny(gray, 50 + can, 255, 1+can2) #cv.adaptiveThreshold(blur,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV,27 + 6 ,3 + can) #cv.Canny(gray, 200 + can, 255, 1+can2) #
    #thershsize = cv.resize(thresh,(960,600))
    #cv.imshow("Gray", gray)
    cv.imshow("Canny", thresh)
    """   
    cnts = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    """
    cnts = [1]
    if cnts is not None:
        """
        for c in cnts:
            
            approxCurve = cv.approxPolyDP(c, len(c) * (0.0002 + (a*0.0001)), True)

            if len(approxCurve) is not 4 or cv.isContourConvex(approxCurve) is False:
                continue #elendi
            
            cv.drawContours(original,[c], 0, (255,0,255), 3)
        print(len(cnts))
        """
        lines = cv.HoughLines(thresh,1,np.pi/180, 150 + a)
        if lines is not None:
            """
            for rho,theta in lines[0]:
                a = np.cos(theta)
                b = np.sin(theta)
                x0 = a*rho
                y0 = b*rho
                x1 = int(x0 + 1000*(-b))
                y1 = int(y0 + 1000*(a))
                x2 = int(x0 - 1000*(-b))
                y2 = int(y0 - 1000*(a))

            cv.line(original,(x1,y1),(x2,y2),(0,0,255),2)
            """
            
            for i in range(0, len(lines)):
                rho = lines[i][0][0]
                theta = lines[i][0][1]
                a = math.cos(theta)
                b = math.sin(theta)
                x0 = a * rho
                y0 = b * rho
                pt1 = (int(x0 + 1000*(-b)), int(y0 + 1000*(a)))
                pt2 = (int(x0 - 1000*(-b)), int(y0 - 1000*(a)))
                cv.line(original, pt1, pt2, (0,0,255), 3, cv.LINE_AA)
            
            print(len(lines))
            lis = []
            circles = 0
            for i in range(50):
                lis.append(len(lines))
            print()
            if circles == 0 and (5 in lis):
                cv.putText(original, 'Switch', (int(original.shape[0]/2),int(original.shape[1]/2)), cv.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2, cv.LINE_AA)
            
    
        
        
        #originalsize = cv.resize(original,(960,600))
        
        cv.imshow("result", original)


if __name__ == '__main__':   
    #image = cv.imread('img/a1.jpg')
    live = cv.VideoCapture(1)
    while True:
        #live_frame = cv.imread('img/switch.jpg')
        ret, live_frame = live.read()
        #ret = True
        """
        dimensions = live_frame.shape
 
        # height, width, number of channels in image
        height = live_frame.shape[0]
        width = live_frame.shape[1]
        channels = live_frame.shape[2]
        
        print('Image Dimension    : ',dimensions)
        print('Image Height       : ',height)
        print('Image Width        : ',width)
        print('Number of Channels : ',channels)
        """
        if ret != False:
            
            cv.namedWindow('Trackbars')
            cv.resizeWindow('Trackbars',640,240)
            cv.createTrackbar('Canny','Trackbars',0,255,nothing)
            cv.createTrackbar('Canny2','Trackbars',0,10,nothing)
            cv.createTrackbar('Approx','Trackbars',0,50,nothing)
            #cv.createTrackbar('X','Trackbars',0,255,nothing)
            #cv.createTrackbar('Y','Trackbars',0,255,nothing)

            #w1 = cv.getTrackbarPos('X','Trackbars')
            #h1 = cv.getTrackbarPos('Y','Trackbars')
            y = 100
            x = 200
            h = int(480/2)
            w = int(640/2) 
            cv.imshow('Original',live_frame)
            crop = live_frame[y:y+h, x:x+w]
            cv.imshow('Image', crop)
            detection(crop)

            k = cv.waitKey(1) & 0xFF
            if k == 27:
                cv.destroyAllWindows()
                break
    live.release()
    cv.destroyAllWindows()
            

    