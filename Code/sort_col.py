#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 11:05:28 2018

@author: ChinasaOkolo
"""

import numpy as np
import matplotlib.pyplot as plt
from numpy import pi as pi
import seaborn as sns
import colorsys
import math

import random

# Not working
colours_length = 1000
colours = []
for i in range(1, colours_length):
	colours.append ([random.random(),random.random(),random.random()])
    
color_palette = sns.palplot(colours)

# Sort colors using in built function
new_colours = colours.sort()  
color_palette2 = sns.palplot(new_colours)

# Sort using hls space
sort_again = colours.sort(key=lambda rgb: colorsys.rgb_to_hsv(*rgb))
color_palette3 = sns.palplot(sort_again)

# Sort with luminosity
def lum (r,g,b):
	return math.sqrt( .241 * r + .691 * g + .068 * b )
sort = colours.sort(key=lambda rgb: lum(*rgb))

color_palette4 = sns.palplot(sort)

def step (r,g,b, repetitions=1):
	lum = math.sqrt( .241 * r + .691 * g + .068 * b )

	h, s, v = colorsys.rgb_to_hsv(r,g,b)

	h2 = int(h * repetitions)
	lum2 = int(lum * repetitions)
	v2 = int(v * repetitions)

	return (h2, lum, v2)
colours.sort(key=lambda (r,g,b): step(r,g,b,8))
