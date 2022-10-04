# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 12:19:59 2022

@author: Ande srikanth
"""
import cv2  
  
# read image as grey scale  
img = cv2.imread(r'D:\images\walpapers\16393.jpg', 1)  
  
# save image  
status = cv2.imwrite(r'D:\images\walpapers\1545048.jpg', 0, img)  
print("Image written to file-system : ", status)  

