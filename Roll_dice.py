# -*- coding: utf-8 -*-
"""
Created on Sat Mar  1 00:39:39 2025

@author: shazi
"""
import random


while True:
    # Ask roll the dice?
    choice = input("Roll the dice? (y/n): ").lower()
    if choice == "y":    # If enter y
        #   generate two random numbers
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6) 
        #   print them
        print(f'({die1}, {die2})')
    elif choice == "n":     # If enter n
        print("Thank you for playing")  #   print thank you msg
        break           #   Terminate the program
    else:
        print("Invalid input")        #   print invalid msg
        

  


