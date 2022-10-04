# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 09:59:21 2022

@author: Ande srikanth
"""

import random
num = random.randint(1,1000)
guess_number = int(input("enter the number you need guess:\n"))
play_again = input("enter y if you need to  play again:\n ")
while play_again == 'y':
    if num == guess_number:
        print("you guessed number is right")
    else :
        print("sorry! you lost")
        """
else:
    print("see you again,bye*_*")
"""
