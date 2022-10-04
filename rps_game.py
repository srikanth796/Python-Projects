# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 22:52:53 2022

@author: Ande srikanth
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 22:17:43 2022

@author: Ande srikanth
"""

#import random module
import random
#rules
rules="winning rules of the rock paper scissor game is as follows:"
rule1 =       "Rock vs Paper->paper wins"
rule2  = "rock vs scissor-> rock wins"
rule3="paper vs scissor->scissor wins"
print(rules)
print(rule1)
print(rule2)
print(rule3)
while "True":
    print("enter your choice\n1.Rock\n2.Paper\n3.scissor")
    choice = int(input("users turn\n"))
    while choice >3 or choice < 1:
        choice = input("please enter a valid option\n")
        
    if choice == 1:
        choice_name = "Rock"
    elif choice == 2:
        choice_name = "Paper"
    elif choice == 3:
        choice_name = "Scissor"
    
    print("users choice is " +choice_name)
    print("its computer turn")
    comp_choice = random.randint(1,3)
    while comp_choice == choice:
        comp_choice = random.randint(1,3)
        
    if comp_choice == 1:
        comp_choice_name = "Rock"
    elif comp_choice == 2:
        comp_choice_name = "Paper"
    elif comp_choice == 3:
        comp_choice_name = "Scissor"
    print("Computer choice is:\n"+ comp_choice_name)
    print(choice_name + "vs"+comp_choice_name)
    if (choice ==1 and comp_choice ==2 ) or (choice ==2 and comp_choice ==1):
        print("Rock wins",end = " ")
        result  = "Paper"
    elif (choice ==1 and comp_choice_name==3)or(choice ==3 and comp_choice ==1):
        print("Scissor Wins",end = " ")
        result = "Rock"
    else :
        print("Scissor")
        result = "Scissor"
        
    if result == choice_name:
        print("you won\n")
        
    else:
        print("computer wins")
    
    ans = input("do you want to play again? (y/n)2")
    if ans == 'n' or ans == 'N':
       break;
       
print("thanks for playing")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    