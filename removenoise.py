# -*- coding: utf-8 -*-
"""removeNoise.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VhAaA6ZoKrv61j4Mcm-uG4uhXxHOqOjS
"""

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
 
from google.colab import files
from io import BytesIO
from PIL import Image

fname='noise.jpg'
uploaded = files.upload()
im = Image.open(BytesIO(uploaded[fname]))

img = cv.imread(fname)
plt.imshow(img)
plt.show()
print(img.shape)

from cv2 import  *
import cv2 
from PIL import Image, ImageFilter
from matplotlib import *
import matplotlib.pyplot as plt
from skimage import data
from skimage.color import rgb2gray
import numpy as np

#mean filter

image = cv2.imread('noise.jpg') # reads the image
image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV) # convert to HSV
figure_size = 9 # the dimension of the x and y axis of the kernal.
new_image = cv2.blur(image,(figure_size, figure_size))
plt.figure(figsize=(11,6))
plt.subplot(121), plt.imshow(cv2.cvtColor(image, cv2.COLOR_HSV2RGB)),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(cv2.cvtColor(new_image, cv2.COLOR_HSV2RGB)),plt.title('Mean filter')
plt.xticks([]), plt.yticks([])
plt.show()

#median filter

new_image = cv2.medianBlur(image, figure_size)
plt.figure(figsize=(11,6))
plt.subplot(121), plt.imshow(cv2.cvtColor(image, cv2.COLOR_HSV2RGB)),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(cv2.cvtColor(new_image, cv2.COLOR_HSV2RGB)),plt.title('Median Filter')
plt.xticks([]), plt.yticks([])
plt.show()

A = cv2.imread('noise.jpg');

#Add gaussian noise with mean 0 and variance 0.59
noise = np.random.normal(0, .59, A.shape)
noisyA = A + noise
plt.imshow(noisyA)
plt.show()

#Adaptive mean filter:

def ad_mean_f(image, window_size):
    """runs the Adaptive Mean Filter proess on an image"""
    xlength, ylength = image.shape #get the shape of the image.
    
    S_xy = window_size
    
    output_image = image.copy()
    
    for row in range(S_xy, xlength-S_xy-1):
        for col in range(S_xy, ylength-S_xy-1):
             filter_window = image[row - S_xy : row + S_xy + 1, col - S_xy : col + S_xy + 1] #filter window
             target = filter_window.reshape(-1) #make 1-dimensional
             var_l =np.var(target)   #local variance
             mean_l =np.mean(target) #local mean
             var_n=np.var(noise)      #variance of noise 
             curr=image[row,col]      #current intensity
             if (var_l != 0):         # exception for local variance = 0
                 new_intensity = curr-var_n/var_l*(curr-mean_l)
             else:
                 new_intensity = curr
             output_image[row, col] = new_intensity
    return output_image

output = ad_mean_f(grayscale_image, 3)
plt.imshow(output)
plt.show()

import numpy as np
import pandas as pd
from PIL import Image, ImageFilter

#Function to convert rgb to grayscale
def rgb2gray(image_rgb):
    if(len(image_rgb.shape) == 3):
        return np.uint8(np.dot(image_rgb[...,:3], [0.2989, 0.5870, 0.1140]))
    else:#already a grayscale
        return image_rgb

image = np.array(noisyA)
grayscale_image = rgb2gray(image)

#Adaptive median Filter

def find_median(array):
    """Return the median of 1-d array"""
    sorted_array = np.sort(array) #timsort (O(nlogn))
    median = sorted_array[len(array)//2]
    return median

def stage_A(z_min, z_med, z_max, z_xy, S_xy, S_max):
    if(z_min < z_med < z_max):
        return stage_B(z_min, z_med, z_max, z_xy, S_xy, S_max)
    else:
        S_xy += 2 #increase the size of S_xy to the next odd value.
        if(S_xy <= S_max): #repeat process
            return stage_A(z_min, z_med, z_max, z_xy, S_xy, S_max)
        else:
            return z_med

def stage_B(z_min, z_med, z_max, z_xy, S_xy, S_max):
    if(z_min < z_xy < z_max):
        return z_xy
    else:
        return z_med

def amf(image, initial_window, max_window):
    """runs the Adaptive Median Filter proess on an image"""
    xlength, ylength = image.shape #get the shape of the image.
    
    z_min, z_med, z_max, z_xy = 0, 0, 0, 0
    S_max = max_window
    S_xy = initial_window #dynamically to grow
    
    output_image = image.copy()
    
    for row in range(S_xy, xlength-S_xy-1):
        for col in range(S_xy, ylength-S_xy-1):
            filter_window = image[row - S_xy : row + S_xy + 1, col - S_xy : col + S_xy + 1] #filter window
            target = filter_window.reshape(-1) #make 1-dimensional
            z_min = np.min(target) #min of intensity values
            z_max = np.max(target) #max of intensity values
            z_med = find_median(target) #median of intensity values
            z_xy = image[row, col] #current intensity
            
           
            new_intensity = stage_A(z_min, z_med, z_max, z_xy, S_xy, S_max)
            output_image[row, col] = new_intensity
    return output_image

output = amf(grayscale_image, 3, 11)
plt.imshow(output)
plt.show()