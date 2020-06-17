#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 16:55:22 2018

@author: ChinasaOkolo
"""

import numpy as np
from PIL import Image
import glob
from colorthief import ColorThief

# Define path of images
directory = '/Users/ChinasaOkolo/Google Drive/SANDISK 8GB/CSCI 195/Code/jpg';

# Create label names
label_1 = 'skintone_1'
label_2 = 'skintone_2'
label_3 = 'skintone_3'
label_4 = 'skintone_4'
label_5 = 'skintone_5'
label_6 = 'skintone_6'

# Get data from file and input into array
fnm = 'muct76-opencv.csv'
data = np.recfromcsv(fnm)

# Variable for holding image list
image_list = []

# Create image list
for filename in glob.glob('cropped_qa/*.jpg'):
    image_list.append(filename)

# Make array to hold colors and palettes
dominant_colors = []
palettes = []

# Iterate through image list 
for i in range(0, len(image_list)): 
    color_thief = ColorThief(image_list[i])

    # Get the dominant color and add to list
    dominant_color = color_thief.get_color(quality=1)
    dominant_colors.append(dominant_color)

    # Build a color palette
    palette = color_thief.get_palette(color_count=6)    
    palettes.append(palette)

# Label images 