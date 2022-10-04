# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 20:10:01 2022

@author: Ande srikanth
"""
import time
from tkinter import *
clock = Tk()
clock.geometry("250x100")
clock.title("Digital clock")
clock.resizable(1,1)
label = Label(clock,font = ("courier",30,"bold"),bg = "pink",fg = "red",bd = 30)
label.grid(row =0,column = 1)
def digitalclock():
    text_input = time.strftime("%H:%M:%S")
    label.config(text=text_input)
    label.after(200, digitalclock)
digitalclock()
clock.mainloop()