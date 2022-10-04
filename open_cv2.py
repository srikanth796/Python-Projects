# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 12:28:35 2022

@author: Ande srikanth
"""

import cv2  
  
# using imread('path') and 0 denotes read as  grayscale image  
path = r'D:\images\walpapers\16393.jpg'
img = cv2.imread(path,1)  
  
#This is using for display the image  
window_name = 'image'
cv2.imshow(window_name,img)  
  
cv2.waitKey(0) # This is necessary to be required so that the image doesn't close immediately.  
#It will run continuously until the key press.  
cv2.destroyAllWindows() 