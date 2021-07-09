#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import numpy as np
import cv2 as cv
"""
live = cv.VideoCapture(0)

while(True):
    
    ret, live_frame = live.read()
    #print(ret)
    if ret != False:
        canny = cv.Canny(live_frame,100,200)
        gray = cv.cvtColor(live_frame, cv.COLOR_BGR2GRAY)
        cv.imshow("Video", live_frame)
        cv.imshow("Canny", canny)
        cv.imshow("Gray", gray)
    
    if cv.waitKey(1) & 0xFF == ord("q"):
        break
    #cv.waitKey(0)    
live.release()
cv.destroyAllWindows()
"""

def nothing(x):
    pass


def detection(frame,origin):
    """
        x1 = cv.getTrackbarPos('X1', 'Trackbars')
        y1 = cv.getTrackbarPos('Y1', 'Trackbars')
        x2 = cv.getTrackbarPos('X2', 'Trackbars')
        y2 = cv.getTrackbarPos('Y2', 'Trackbars')
    """
    original = origin.copy()
    #base = origin.copy()
        #deneme = frame.copy()
        #circle = cv.getTrackbarPos('circle','Trackbars')    
        #para1 = cv.getTrackbarPos('param 1','Trackbars')
        #para2 = cv.getTrackbarPos('param 2','Trackbars')
    minRadiu = cv.getTrackbarPos('min Radius','Trackbars')
    maxRadiu = cv.getTrackbarPos('max Radius','Trackbars')
    circles = cv.HoughCircles(frame,cv.HOUGH_GRADIENT,2,1 + 171, param1 = 50, param2 = 20 + 57, minRadius = 0 + minRadiu, maxRadius = 0 + maxRadiu) # 14 ile 132
   
    if circles is not None:
        
    
        counter = len(circles[0,:])
        print("Circle count: " + str(counter))
        circles = np.uint16(np.around(circles))
        #print(circles[0,:]) ((i[0] - 10/2), (i[1] - 10/2)), ((i[0] + 10/2), (i[1] + 10/2))
            
        for i in circles[0,:]:
            #img = cimg.copy()
            #img = cv.cvtColor(cimg,cv.COLOR_GRAY2RGB)
            # draw the outer circle
            cv.circle(original,(i[0],i[1]),i[2],(0,255,0),2)
            # draw the center of the circle
            cv.circle(original,(i[0],i[1]),2,(0,0,255),3)
            """
            cv.circle(deneme,(i[0],i[1]),i[2],(0,255,0),2)
            # draw the center of the circle
            cv.circle(deneme,(i[0],i[1]),2,(0,0,255),3)
            cv.imshow("deneme",deneme)
            """
            """
            if counter == 2:
                #cv.putText(img, 'Socket', (i[0], i[1]), cv.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 2, cv.LINE_AA)
                pass
            else:
                pass

            #cv.putText(img, 'Somthing Else', (i[0], i[1]), cv.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 2, cv.LINE_AA)
            #cv.rectangle(img,(i[0] + 536, i[1] + 457), (i[0] - 541, i[1] - 529),(0,255,0),3)
            #print(i[0],i[1])
            """
            
            #cv.imshow('Original',base)
            cv.imshow('Plug',original)
            
            """ 
            cimg  = cv.imread('img/f_type_socket.png',0)
            cimg = cv.medianBlur(cimg,5)
            #cimg = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
            #cv.namedWindow('Trackbars')
            """
   
if __name__ == '__main__':
    live = cv.VideoCapture(1)
    
    while(True):
    
        ret, live_frame = live.read()
        if ret != False:
            gray = cv.cvtColor(live_frame, cv.COLOR_BGR2GRAY)
            blur = cv.medianBlur(gray,5)
            cimg = cv.adaptiveThreshold(blur,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV,27,3) #cv.threshold(gray, 1 + 108, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)[1]
                
            cv.namedWindow('Trackbars')
            cv.resizeWindow('Trackbars',640,240)

            #cv.createTrackbar('circle', 'Trackbars',0,255,nothing)
            #cv.createTrackbar('param 1','Trackbars',0,255,nothing)
            #cv.createTrackbar('param 2','Trackbars',0,255,nothing)
            cv.createTrackbar('min Radius','Trackbars',0,100,nothing)
            cv.createTrackbar('max Radius','Trackbars',0,100,nothing)

            y = 100
            x = 200
            h = int(480/2)
            w = int(640/2) 
            cv.imshow('Original',live_frame)
            crop = cimg[y:y+h, x:x+w]
            crop2 = live_frame[y:y+h, x:x+w]
            cv.imshow('Image', crop)
            
            detection(crop,crop2)
            
            if cv.waitKey(1) & 0xFF == ord("q"):
                break
    live.release()
    cv.destroyAllWindows()


