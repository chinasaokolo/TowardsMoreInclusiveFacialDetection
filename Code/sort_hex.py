#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 11:56:11 2018

@author: ChinasaOkolo
"""

import numpy as np
import matplotlib.pyplot as plt
from numpy import pi as pi

import colorsys

def get_hsv(hexrgb):
    hexrgb = hexrgb.lstrip("#")   # in case you have Web color specs
    r, g, b = (int(hexrgb[i:i+2], 16) / 255.0 for i in range(0,5,2))
    return colorsys.rgb_to_hsv(r, g, b)

color_list = ['633d3a', '81524c', 'f524c', "40231f"]  # GBR
color_list.sort(key=get_hsv)
print(color_list)