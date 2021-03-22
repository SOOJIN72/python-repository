# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 16:11:36 2021

@author: 82105
"""

import cv2
import glob 

for image in glob.glob('*.jpg')
    
    fname = image 
    img_gray = cv2.imread(fname, 0) # 0: gray; 1, RGB; -1: transparency
    img_color = cv2.imread(fname, 1)
   
    
    img_gnew = cv2.resize(img_gray, (300, 300))
    img_cnew = cv2.resize(img_color, (300, 300))
  
    
    # cv2.imshow('Gray', img_gray)
    # cv2.imshow('Color', img_color)
    cv2.imshow('Gray', img_gnew)
    cv2.imshow('Color', img_cnew)
   

    fname_new = image + "_resized.jpg"
    cv2.imwrite(fname_new, img_cnew)
    cv2.waitKey(2000) # 0: press button; 2000: 2 seconds
    cv2.destroyAllWindows()
    