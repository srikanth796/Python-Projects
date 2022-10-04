# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 08:30:37 2022

@author: Ande srikanth
"""

#Age calculator
from tkinter import *
from tkinter import messagebox
def clearAll():
    dayField.delete(END,0)
    monthField.delete(END,0)
    yearField.delete(END,0)