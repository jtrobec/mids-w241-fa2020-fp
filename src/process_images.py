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


def display_image_set(images, titles=[]):
    (fig, ax) = plt.subplots(1, len(images), figsize=(20,20), sharey=True)
    for x in range(len(images)):
        ax[x].imshow(cv2.cvtColor(images[x], cv2.COLOR_BGR2RGB))
        if len(titles) == len(images):
            ax[x].set_title(titles[x])
    plt.show()

def main(argv):
   inputfile = ''
   try:
      opts, args = getopt.getopt(argv,"hi:",["ifile="])
      print(opts)
   except getopt.GetoptError:
      print ('process_images.py -i <experiment_dir>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print ('process_images.py -i <experiment_dir>')
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
   print("Experiment Directory: {}".format(inputfile))
   exp_images = ExperimentImages(inputfile)
   print(exp_images.list_times())
   print(exp_images.list_subjects())
   images = exp_images.get_subject_images('a1')
   display_image_set(images, exp_images.list_times())

if __name__ == "__main__":
   main(sys.argv[1:])
