# -*- coding: utf-8 -*-
#import os
# os.getcwd()
# os.chdir("C:\\Users\\Koohong\\Documents\\MIDS\MIDS241")

import cv2
import numpy as np
# =============================================================================
# import matplotlib.pyplot as plt
# =============================================================================

#======================================
## NOW Select the filtering values
# Trackbars to find the optimal value
#Color detection
#======================================

def empty(a):
    pass

#resize the picture, does not change the quality of the picture
path = 'mids-w241-fa2020-fp/data/B/experiment2/t1/s2t1.jpg'


# =============================================================================
# ######################################################
# # HSA selection process
# #
# ######################################################
# #the name given to window needs to be the same
# #the name of the window is TrackBars
# cv2.namedWindow("TrackBars")
# cv2.resizeWindow("TrackBars",740,340)
# 
# #Hue has max value of 360, but opencv only supports
# #upto 180
# # HSA reference
# # http://colorizer.org/#:~:text=HSL%20color%20space&text=Ranges%20from%200%20to%20360%C2%B0%20in%20most%20applications%20(each,is%20a%20shade%20of%20yellow).
# # based on the information above, set the HSA
# 
# cv2.createTrackbar("Hue Min","TrackBars",0,179,empty)
# cv2.createTrackbar("Hue Max","TrackBars",179,179,empty)
# cv2.createTrackbar("Sat Min","TrackBars",0,255,empty)
# cv2.createTrackbar("Sat Max","TrackBars",255,255,empty)
# cv2.createTrackbar("Val Min","TrackBars",0,255,empty)
# cv2.createTrackbar("Val Max","TrackBars",255,255,empty)
# 
# 
# 
# while True:
#     img = cv2.imread(path)
#     img = cv2.resize(img,(300,400))
# 
#     #convert to HSA
#     imgHSV = cv2.cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#     #define hue, satuaration and value
#     h_min = cv2.getTrackbarPos("Hue Min","TrackBars")
#     h_max = cv2.getTrackbarPos("Hue Max","TrackBars")
#     s_min = cv2.getTrackbarPos("Sat Min","TrackBars")
#     s_max = cv2.getTrackbarPos("Sat Max","TrackBars")
#     v_min = cv2.getTrackbarPos("Val Min","TrackBars")
#     v_max = cv2.getTrackbarPos("Val Max","TrackBars")
# 
#     print(h_min,h_max,s_min,s_max,v_min,v_max)
#     
#     #select the filtered image
#     lower = np.array([h_min,s_min,v_min])
#     upper = np.array([h_max,s_max,v_max])
#     
#     #filtered image
#     mask = cv2.inRange(imgHSV, lower, upper)
#     
#     #using filtered images to create new image 
#     #this is adding two images together
#     
#     imgResult = cv2.bitwise_and(img,img, mask = mask)
#     
#     cv2.imshow("Original",img)
#     cv2.imshow("HSA",imgHSV)
#     cv2.imshow("Mask",mask)
#     cv2.imshow("result",imgResult)
#     cv2.waitKey(1)
# =============================================================================


#############################################
# After selecting the correct HSV
#############################################
img = cv2.imread(path)
img = cv2.resize(img,(300,400))

#convert to HSA
imgHSV = cv2.cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#select the filtered image
lower = np.array([21,36,44])
upper = np.array([55,255,255])

#filtered image
mask = cv2.inRange(imgHSV, lower, upper)

#using filtered images to create new image 
#this is adding two images together 
imgResult = cv2.bitwise_and(img,img, mask = mask)

## NOW Select the filtering values
# =============================================================================
# ## Canny detection
kernel = np.ones((5,5),np.uint8)
imgCanny = cv2.Canny(imgResult,150,200)

# imgDialation = cv2.dilate(imgCanny,kernel, iterations = 3)
# img

cv2.imshow("Original",img)
cv2.imshow("HSA",imgHSV)
cv2.imshow("Mask",mask)
cv2.imshow("result",imgResult)
cv2.imshow("Canny", imgCanny)
cv2.waitKey(0)





# plt.imshow(imgDialation)
# =============================================================================

#after running rough edges, then we need to get the countours
