#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 11:18:14 2018

@author: ChinasaOkolo
"""

import numpy as np
import matplotlib.pyplot as plt
from numpy import pi as pi
import random
import seaborn as sns
from random import randint
import math

colours_length = 1000
colours = []

#for i in range(1, colours_length):
#	colours.append ([randint(0, 255), randint(0, 255), randint(0, 255)])

for i in range(1, colours_length):
	colours.append ([random.random(), random.random(),random.random()])

# Sort colours
colours.sort()

def lum (r,g,b):
	return math.sqrt( .241 * r + .691 * g + .068 * b )
colours.sort(key=lambda rgb: lum(*rgb)	)

def step (r,g,b, repetitions=1):
	lum = math.sqrt( .241 * r + .691 * g + .068 * b )

	h, s, v = colorsys.rgb_to_hsv(r,g,b)

	h2 = int(h * repetitions)
	lum2 = int(lum * repetitions)
	v2 = int(v * repetitions)

	return (h2, lum, v2)

colours.sort(key = step(r,g,b,8))

# Create sorted color palette
sorted_color_palette = sns.palplot(sorted)  