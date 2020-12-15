#!/usr/bin/env python3

import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from functools import reduce
from process_images import display_image_set, image_resize
from PIL import Image

nobu_image_names =     ['ta1', 'ca2', 'ta3', 'ca4', 'cb1', 'tb2', 'cb3', 'tb4', 'cc1', 'tc2', 'cc3', 'tc4']
nobu_new_image_names = ['t1',  'c2',  't3',  'c4',  'c5',  't6',  'c7',  't8',  'c9',  't10', 'c11', 't12']
nobu_avocado_images = ['./data/N/experiment4/after_cutting/{}.jpg'.format(x) for x in nobu_image_names]
justin_image_names = ['t1', 't4', 't7', 't8', 't9', 't11', 'c2', 'c3', 'c5', 'c6', 'c10', 'c12']
justin_avocado_images = ['./data/J/experiment3/{}.jpg'.format(x) for x in justin_image_names]
bill_image_names = ['c1', 'c6', 'c8', 'c9', 'c11', 'c12', 't2', 't3', 't4', 't5', 't7', 't10']
bill_avocado_images = ['./data/B/experiment4/{}.jpg'.format(x) for x in bill_image_names]

def load_avocado_images(image_file_paths):
    images = [cv2.imread(im_path) for im_path in image_file_paths]
    return images

def set_consistent_width(images):
    max_width = np.max([x.shape[1] for x in images])
    resized = [image_resize(i, width=max_width) for i in images]
    return resized

def crop_avocado_image_1(img):
    #convert to HSA
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    #select the filtered image
    lower = np.array([19,19,19])
    upper = np.array([55,255,255])
    #filtered image
    mask = cv2.inRange(imgHSV, lower, upper)
    #using filtered images to create new image 
    #this is adding two images together 
    imgResult = cv2.bitwise_and(img,img, mask = mask)
    imgGray = cv2.cvtColor(imgResult, cv2.COLOR_BGR2GRAY)
    #sigma, the higher the value, the more blur you get
    imgBlur = cv2.GaussianBlur(imgGray,(7,7),1)

    (cnts, _) = cv2.findContours(imgBlur, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) 
    maxArea = 0
    bestRect = (0,0,0,0)
    bestCnt = None
    for c in cnts: 
        area = cv2.contourArea(c)
        if area > maxArea:
            maxArea = area
            x,y,w,h = cv2.boundingRect(c)
            bestRect = (x,y,w,h)
            bestCnt = c
    mask = np.zeros(img.shape, np.uint8)
    cv2.drawContours(mask, [bestCnt], -1, (255,255,255), -1)
    mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
    imgResult = cv2.bitwise_and(img, img, mask=mask)
    
    x,y,w,h = bestRect
    new_img = imgResult[y:y+h,x:x+w] 
    return new_img

def crop_avocado_image_2(img):
    #convert to HSA
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    #select the filtered image
    lower = np.array([21,36,44])
    upper = np.array([55,255,255])
    #filtered image
    mask = cv2.inRange(imgHSV, lower, upper)
    #using filtered images to create new image 
    #this is adding two images together 
    imgResult = cv2.bitwise_and(img,img, mask = mask)
    imgGray = cv2.cvtColor(imgResult, cv2.COLOR_BGR2GRAY)
    #sigma, the higher the value, the more blur you get
    imgBlur = cv2.GaussianBlur(imgGray,(7,7),1)

    (cnts, _) = cv2.findContours(imgBlur, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) 
    maxArea = 0
    bestRect = (0,0,0,0)
    bestCnt = None
    for c in cnts: 
        area = cv2.contourArea(c)
        if area > maxArea:
            maxArea = area
            x,y,w,h = cv2.boundingRect(c)
            bestRect = (x,y,w,h)
    
    x,y,w,h = bestRect
    new_img = imgResult[y:y+h,x:x+w] 
    return new_img

def crop_avocado_images(images, method):
    cropped = [method(img) for img in images]
    return cropped

def get_blackness_percentage(image):
    black = [0, 0, 0]  # RGB for black
    diff = 30
    boundaries = [([black[2], black[1], black[0]],
                [black[2]+diff, black[1]+diff, black[0]+diff])]
    # in order BGR as opencv represents images as numpy arrays in reverse order

    lower, upper = boundaries[0]

    lower = np.array(lower, dtype=np.uint8)
    upper = np.array(upper, dtype=np.uint8)
    mask = cv2.inRange(image, lower, upper)
    output = cv2.bitwise_and(image, image, mask=mask)

    ratio_black = cv2.countNonZero(mask)/(image.size/3)
    return np.round(ratio_black*100, 2)

def get_blackness_percentage_for_hue(img, hue):
    #convert to HSA
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    #reading the values from trackbar
    #define hue, satuaration and value
    h_min, h_max = (hue, 179)
    s_min, s_max = (0, 255)
    v_min, v_max = (0, 255)
    
    #select the filtered image
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    
    #filtered image
    mask = cv2.inRange(imgHSV, lower, upper)
    
    #using filtered images to create new image 
    #this is adding two images together
    imgResult = cv2.bitwise_and(img,img, mask = mask)
    blackness = get_blackness_percentage(imgResult)
    return blackness

def main():
    avo_image_lists = [('B', bill_image_names, bill_avocado_images), 
                        ('N', nobu_image_names, nobu_avocado_images), 
                        ('J', justin_image_names, justin_avocado_images)]

    dataframes = []
    for block_id, img_names, img_list in avo_image_lists:
        images = load_avocado_images(img_list)
        sized = set_consistent_width(images)
        cropped = crop_avocado_images(sized, crop_avocado_image_1)
        # display_image_set([images, sized, cropped], img_names)
        black_pct = []
        for img in cropped:
            black_pct.append([get_blackness_percentage_for_hue(img, hue) for hue in range(50)])
        if block_id == 'N':
            img_names = nobu_new_image_names
        names_blocked = ['{}{}'.format(block_id, x) for x in img_names]
        data = { k:v for (k,v) in zip(names_blocked, black_pct) }
        df = pd.DataFrame(data, columns=names_blocked)
        dataframes.append(df)

    final_data = reduce(lambda x, y: pd.concat([x, y], axis=1), dataframes)
    final_data.index.name = 'hue_index'
    print(final_data)
    final_data.to_csv('avocado_blackness.csv')
    

if __name__ == "__main__":
    main()
