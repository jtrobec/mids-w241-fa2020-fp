#!/usr/bin/env python3

import cv2
import getopt
import imutils
import matplotlib.pyplot as plt
import numpy as np
import PIL
import sys

from experiment_images import ExperimentImages
from PIL import Image

def get_contour_box(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # convert to grayscale
    # threshold to get just the signature (INVERTED)
    retval, thresh_gray = cv2.threshold(gray, thresh=100, maxval=255, type=cv2.THRESH_BINARY_INV)
    contours, hierarchy = cv2.findContours(thresh_gray,cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    # Find object with the biggest bounding box
    mx = (0,0,0,0)      # biggest bounding box so far
    mx_area = 0
    for cont in contours:
        x,y,w,h = cv2.boundingRect(cont)
        area = w*h
        if area > mx_area:
            mx = x,y,w,h
            mx_area = area
    # slightly enlarge box
    x,y,w,h = mx
    mx = (x-1, y-1, w+1, h+1)
    return mx

def add_contour_box(img):
    mx = get_contour_box(img)
    x,y,w,h = mx
    cp = img.copy()
    cv2.rectangle(cp,(x,y),(x+w,y+h),(200,0,0),2)
    return cp

def crop_image(img):
    mx = get_contour_box(img)
    x,y,w,h = mx
    cp = img[y:y+h, x:x+w]
    return cp

def display_image_set(images, titles=[]):
    (fig, ax) = plt.subplots(len(images), len(images[0]), figsize=(20,15), sharey=True, sharex=True)
    for x in range(len(images)):
        for y in range(len(images[x])):
            if (len(images)) == 1:
                ax[y].imshow(cv2.cvtColor(images[x][y], cv2.COLOR_BGR2RGB))
                if len(titles) == len(images[x]):
                    ax[y].set_title(titles[y])
            else:
                ax[x][y].imshow(cv2.cvtColor(images[x][y], cv2.COLOR_BGR2RGB))
                if len(titles) == len(images[x]):
                    ax[x][y].set_title(titles[y])
    fig.tight_layout()
    plt.subplots_adjust(hspace=0.1, wspace=0.1)
    plt.show()

# from stackoverflow: https://stackoverflow.com/questions/44650888/resize-an-image-without-distortion-opencv
def image_resize(image, width = None, height = None, inter = cv2.INTER_AREA):
    # initialize the dimensions of the image to be resized and
    # grab the image size
    dim = None
    (h, w) = image.shape[:2]

    # if both the width and height are None, then return the
    # original image
    if width is None and height is None:
        return image

    # check to see if the width is None
    if width is None:
        # calculate the ratio of the height and construct the
        # dimensions
        r = height / float(h)
        dim = (int(w * r), height)

    # otherwise, the height is None
    else:
        # calculate the ratio of the width and construct the
        # dimensions
        r = width / float(w)
        dim = (width, int(h * r))

    # resize the image
    resized = cv2.resize(image, dim, interpolation = inter)

    # return the resized image
    return resized

def main(argv):
    inputfile = ''
    try:
        opts, args = getopt.getopt(argv,"hi:s:",["ifile=","subj="])
        print(opts)
    except getopt.GetoptError:
        print ('process_images.py -i <experiment_dir> -s <subject_id>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('process_images.py -i <experiment_dir> -s <subject_id>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-s", "--subj"):
            subj = arg

    print("Experiment Directory: {}".format(inputfile))
    print("Subject: {}".format(subj))
    exp_images = ExperimentImages(inputfile)
    print(exp_images.list_times())
    print(exp_images.list_subjects())
    images = exp_images.get_subject_images(subj)
    display_image_set([images, images], exp_images.list_times())
    #boxed = [add_contour_box(img) for img in images]
    #cropped = [crop_image(img) for img in images]
    #display_image_set([images, boxed, cropped], exp_images.list_times())


if __name__ == "__main__":
    main(sys.argv[1:])
