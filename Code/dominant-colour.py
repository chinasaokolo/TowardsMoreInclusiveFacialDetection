#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 23:57:47 2018

@author: ChinasaOkolo
"""

import os, sys
import numpy as np
from PIL import Image
import glob
from colorthief import ColorThief
import colorsys
import seaborn as sns

image = Image.open('new_qa3.jpg')

def most_frequent_colour(image):

    w, h = image.size
    pixels = image.getcolors(w * h)

    most_frequent_pixel = pixels[0]

    for count, colour in pixels:
        if count > most_frequent_pixel[0]:
            most_frequent_pixel = (count, colour)


    return most_frequent_pixel

    #print(most_frequent_pixel)