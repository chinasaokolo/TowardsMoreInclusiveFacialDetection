#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 18:20:41 2018

@author: ChinasaOkolo
"""

import os, sys
import numpy as np
from PIL import Image
import glob
from colorthief import ColorThief
import colorsys
import seaborn as sns


# Get data from file and input into array
fnm = 'muct76-oc_forehead.csv'
data_fh = np.recfromcsv(fnm)

# Variable for holding image list
fhimage_list = []

# Create image list
for filename in glob.glob('qa_only/*.jpg'):
    fhimage_list.append(filename)
        
# Crop images
for i in range(0, len(data_fh)):  
    im = Image.open(fhimage_list[i])    
    area = (data_fh[i][3], data_fh[i][4], data_fh[i][1], data_fh[i][2])  
    crop_img = im.crop(area)
    save_img = crop_img.save('new_fh'+ str(i) + '.jpg')

# Make array to hold colors and palettes
dominant_fhcolors = []
fh_palettes = []

# Iterate through image list 
for i in range(0, len(fhimage_list)): 
    color_thief = ColorThief(fhimage_list[i])

    # Get the dominant color and add to list
    dominant_color = color_thief.get_color(quality=1)
    dominant_fhcolors.append(dominant_color)

    # Build a color palette
    palette = color_thief.get_palette(color_count=6)    
    fh_palettes.append(palette)

# Hex values for dominant colors
dominant_hexfh = []    

# Convert color palette from RGB to hex
for i in range(0, len(dominant_fhcolors)): 
    hex_color = '#%02x%02x%02x' % (dominant_fhcolors[i])
    dominant_hexfh.append(hex_color)
    
# Make list to hold color of middle pixels
fh_pixels = []
    
# Get color of middle pixel of cropped forehead image
for filename in glob.glob('*.jpg'):
    im = Image.open(filename)
    width, height = im.size
    middle_pixel = (width/2,height/2)
    pix = im.load()
    color_pixel = pix[middle_pixel]
    fh_pixels.append(color_pixel)

# Get hex value of middle pixels   
hex_fhpixels = []

# Create unsorted color palette
color_palette = sns.palplot(hex_fhpixels)

# Convert color palette from RGB to hex
for i in range(0, 91): 
    hex_color = '#%02x%02x%02x' % (fh_pixels[i])
    hex_fhpixels.append(hex_color)   
    
# Define function to sort hex values    
def get_hsv(hexrgb):
    hexrgb = hexrgb.lstrip('#')   # in case you have Web color specs
    r, g, b = (int(hexrgb[i:i+2], 16) / 255.0 for i in range(0,5,2))
    return colorsys.rgb_to_hsv(r, g, b)

# Sort hex values
sortedhex_list = list(hex_fhpixels) # GBR
sortedhex_list.sort(key=get_hsv) 

# Define function to return RGB values
def get_rgb(hex):
    h = hex.lstrip('#')
    r, g, b = (tuple(int(h[i:i+2], 16) for i in (0, 2 ,4)))
    return (r, g, b)

# Create sorted RGB list
sortedrgb_list = []

# Return sorted RGB values
for i in range(0, 91): 
    rgb_color = get_rgb(sortedhex_list[i])  
    sortedrgb_list.append(rgb_color)
    
# Create sorted color palette
sorted_color_palette = sns.palplot(sortedhex_list)

# Create mapping between image name and hex/rgb values
hex_dict = {}
rgb_dict = {}

for i in range(0, 91):
    hex_dict.update( {fhimage_list[i] : (hex_fhpixels[i])} ) 
    rgb_dict.update( {fhimage_list[i] : (fh_pixels[i])} ) 
    
# Create list for sorted names
sorted_names = []
    
for i in range(0, 91):
    sort_hexkey = (list(hex_dict.keys())[list(hex_dict.values()).index(sortedhex_list[i])])
    
    # Add names to list
    sorted_names.append(sort_hexkey)
    
# Create mapping between image names and sorted hex/rgb values
hex_sortlist = []
rgb_sortlist = []
sorted_tuplelist = []

# Create label names
label_1 = 'skintone_1'
label_2 = 'skintone_2'
label_3 = 'skintone_3'
label_4 = 'skintone_4'
label_5 = 'skintone_5'
label_6 = 'skintone_6'

for i in range(0, 91):
    hex_sortlist.append((sorted_names[i], sortedhex_list[i]))
    rgb_sortlist.append((sorted_names[i], sortedrgb_list[i])) 
    
    # Add labels to tuple list while adding names
    if (i < 15):
        sorted_tuplelist.append((sorted_names[i], sortedhex_list[i], sortedrgb_list[i], label_1)) 
    elif (i < 30):
        sorted_tuplelist.append((sorted_names[i], sortedhex_list[i], sortedrgb_list[i], label_2)) 
    elif (i < 45):
        sorted_tuplelist.append((sorted_names[i], sortedhex_list[i], sortedrgb_list[i], label_3)) 
    elif (i < 60):
        sorted_tuplelist.append((sorted_names[i], sortedhex_list[i], sortedrgb_list[i], label_4)) 
    elif (i < 75):
        sorted_tuplelist.append((sorted_names[i], sortedhex_list[i], sortedrgb_list[i], label_5)) 
    else:
        sorted_tuplelist.append((sorted_names[i], sortedhex_list[i], sortedrgb_list[i], label_6)) 
     
 
# Remove outliers of sorted hex list
new_sorted_hex_list = sortedhex_list 

# Switching indexes in file
  # i = ['title', 'email', 'password2', 'password1', 'first_name', 
   #      'last_name', 'next', 'newsletter']
    #a, b = i.index('password2'), i.index('password1')
    #i[b], i[a] = i[a], i[b]
    
    
    
    
    
    
    
    