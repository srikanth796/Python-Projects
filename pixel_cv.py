# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 19:13:36 2022

@author: Ande srikanth
"""
import cv2
import numpy as np
path = r'D:\images\walpapers\minion.jpg'
image = cv2.imread(path,0)
pixel = image[100,100]
print(pixel)