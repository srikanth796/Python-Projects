# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 18:38:59 2022

@author: Ande srikanth
"""

# Python program to explain cv2.imshow() method 
  
# importing cv2 
import cv2 
  
# path 
path = r'D:\images\walpapers\16393.jpg'
  
# Reading an image in default mode
image = cv2.imread(path,0)
  
# Window name in which image is displayed
window_name = 'image'
  
# Using cv2.imshow() method 
# Displaying the image 
cv2.imshow(window_name, image)
  
#waits for user to press any key 
#(this is necessary to avoid Python kernel form crashing)
cv2.waitKey(0) 
  
#closing all open windows 
cv2.destroyAllWindows() 