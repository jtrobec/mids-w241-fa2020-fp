# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 22:07:59 2020

@author: Koohong
"""

import cv2
import numpy as np

def getContours(img):
    #gets the extreme outer countour, RETR_EXTERNAL
    contours,hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        #area of all the shapes that we have detected
        area = cv2.contourArea(cnt)
        #print(area)
        #cnt is the contour that we found
        #-1 for drawing all the countours
        #cv2.drawContours(imgContour,cnt,-1,(255,0,0),3)
        
        #you can give minimum area for detection
        # 500 pixles
        if area > 1000:
            cv2.drawContours(imgContour,cnt,-1,(255,0,0),3)
            #if you want to draw bounding box
            peri = cv2.arcLength(cnt,True) #enclosed one
            print(peri)
            #approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
            #tells you number of corners in a closed shape
            #print(len(approx))
            #objCor = len(approx)
            #drawing bounding box.
# =============================================================================
#             x,y,w,h = cv2.boundingRect(approx)
#             cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0),2)
# =============================================================================


path = 'mids-w241-fa2020-fp/data/B/experiment2/t1/s2t1.jpg'
img = cv2.imread(path)
img = cv2.resize(img,(300,400)) #original is too big

#image that will be used inside getContour
imgContour = img.copy()

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#sigma, the higher the value, the more blur you get
imgBlur = cv2.GaussianBlur(imgGray,(7,7),1)

##############################################


#canny
imgCanny = cv2.Canny(imgBlur, 50,50)


getContours(imgCanny)

#just black images
imgBlank = np.zeros_like(img)



#=============================================================================
cv2.imshow("Original", img)
cv2.imshow("gray", imgGray)
cv2.imshow("blur", imgBlur)
cv2.imshow("canny",imgCanny)
cv2.imshow("contour",imgContour)
cv2.waitKey(0)

