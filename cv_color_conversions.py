# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 08:23:49 2022

@author: Ande srikanth
"""

import cv2 as cv
path = r"D:\images\@family\Dhishan\IMG-20210118-WA0103.jpg"
#reading the colour path
src = cv.imread(path)
window_name = 'image'
#conversion of image colour using cv.cvtolor() method
colorcnvt = cv.cvtColor(src,cv.COLOR_BGR2GRAY)
cv.imshow(window_name,src)