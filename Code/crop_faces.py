#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 00:43:16 2018

@author: ChinasaOkolo
"""

import numpy as np
from PIL import Image
import glob
from colorthief import ColorThief

# Get data from file and input into array
fnm = 'muct76-opencv_orig.csv'
data_orig = np.recfromcsv(fnm)

# Variable for holding image list
qaimage_list = []

# Create image list
for filename in glob.glob('qa_only/*.jpg'):
    qaimage_list.append(filename)
        
# Crop images
for i in range(0, len(data_orig)):  
    im = Image.open(qaimage_list[i])    
    area = (data_orig[i][1], data_orig[i][2], data_orig[i][5], data_orig[i][4])  
    crop_img = im.crop(area)
    save_img = crop_img.save('new_qa'+ str(i) + '.jpg')

# Make array to hold colors and palettes
dominant_qacolors = []
qa_palettes = []

# Iterate through image list 
for i in range(0, len(qaimage_list)): 
    color_thief = ColorThief(qaimage_list[i])

    # Get the dominant color and add to list
    dominant_color = color_thief.get_color(quality=1)
    dominant_qacolors.append(dominant_color)

    # Build a color palette
    palette = color_thief.get_palette(color_count=6)    
    qa_palettes.append(palette)

# Hex values for dominant colors
dominant_hexqa = []    

# Convert color palette from RGB to hex
for i in range(0, len(dominant_qacolors)): 
    hex_color = '#%02x%02x%02x' % (dominant_qacolors[i])
    dominant_hexqa.append(hex_color)
    
    