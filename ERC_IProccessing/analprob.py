#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np 
import cv2 as cv

def nothing(x):
    pass

def color_detection(frame, lis):
    original = frame.copy()
    hsv_frame = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    low_green = np.array([69, 122, 35])
    high_green = np.array([179, 255, 255])
    green_mask = cv.inRange(hsv_frame, low_green, high_green)
    green = cv.bitwise_and(frame, frame, mask=green_mask)
    green_count = np.count_nonzero(green) / green.size
    cv.imshow("Mask", green_mask)
    cv.imshow("Green", green)
    cnts = cv.findContours(green_mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    # Extract contours depending on OpenCV version
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]

    # Iterate through contours and filter by the number of vertices 
    for c in cnts:
        perimeter = cv.arcLength(c, True)
        x,y,w,h = cv.boundingRect(c)
        approx = cv.approxPolyDP(c, 0.04 * perimeter, True)
        if len(approx) > 5:
            cv.drawContours(original, [c], -1, (0, 0, 255), -1)
            cv.circle(original,(461 + lis[6],497 - lis[7]), 109 - lis[8], (0,255,0), 5)
            cv.putText(original, 'Probe', (x,y-5), cv.FONT_HERSHEY_SIMPLEX, 1, (2,249,249), 2, cv.LINE_AA)
            #print([c][0][1])

    #cv.imshow('green_mask', green_mask)
    cv.imshow('Probe', original)
    


img  = cv.imread('img/probalt.jpeg')

cv.imshow('Prob',img)
cv.namedWindow('Trackbars')

cv.resizeWindow('Trackbars',640,240)
cv.createTrackbar("L - H", "Trackbars", 0, 179, nothing)
cv.createTrackbar("L - S", "Trackbars", 0, 255, nothing)
cv.createTrackbar("L - V", "Trackbars", 0, 255, nothing)
cv.createTrackbar("U - H", "Trackbars", 179, 179, nothing)
cv.createTrackbar("U - S", "Trackbars", 255, 255, nothing)
cv.createTrackbar("U - V", "Trackbars", 255, 255, nothing)
cv.createTrackbar("X", "Trackbars", 0, 400,nothing)
cv.createTrackbar("Y", "Trackbars", 0, 400, nothing)
cv.createTrackbar("THICC", "Trackbars", 0, 300,nothing)

while True:
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        cv.destroyAllWindows()
        break

    x = cv.getTrackbarPos("X", "Trackbars")
    y = cv.getTrackbarPos("Y", "Trackbars")
    l_h = cv.getTrackbarPos("L - H", "Trackbars")
    l_s = cv.getTrackbarPos("L - S", "Trackbars")
    l_v = cv.getTrackbarPos("L - V", "Trackbars")
    u_h = cv.getTrackbarPos("U - H", "Trackbars")
    u_s = cv.getTrackbarPos("U - S", "Trackbars")
    u_v = cv.getTrackbarPos("U - V", "Trackbars")    
    thicc = cv.getTrackbarPos("THICC", "Trackbars")

    lis = [l_h, l_s, l_v, u_h, u_s, u_v , x, y, thicc]
    print("Low H: " + str(lis[0]) + " Low S: " + str(lis[1]) + " Low V: " + str(lis[2]))
    color_detection(img, lis)

#cv.waitKey(0)
#cv.destroyAllWindows()