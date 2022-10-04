# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 19:29:50 2022

@author: Ande srikanth
"""

import cv2
image = cv2.imread(r'D:\images\walpapers\minion.jpg')
height = image.shape[0]
width = image.shape[1]
channels=image.shape[2]
size =image.size
#print("image dimension:",dimensions)
print("height:",height)
print("width:",width)
print("channels:",channels)
print("image size:",size)