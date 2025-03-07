# -*- coding: utf-8 -*-
"""
Created on Fri Mar  7 12:23:48 2025

@author: shazid
"""
    
import random

choices = ("r", "p", "s")

def get_choices():
    while True:
        rps_choice = input("Choose Rock, Paper, Scissor? (r, p, s): ").lower()
        if rps_choice in choices:
            return rps_choice
        else:
            print("Invalid input")
    
def show_choices(rps_choice, pc_choice):
    print(f'You choose {rps_choice}')
    print(f'Computer choose {pc_choice}')

def determine_winner(rps_choice, pc_choice):
    if rps_choice == pc_choice:
        print("Draw")
    elif ((rps_choice=="r" and pc_choice=="s") or 
          (rps_choice=="p" and pc_choice=="r") or
          (rps_choice=="s" and pc_choice=="p")):
        print("You WIn!")
    else:
        print("You Lose!")

def play_game():        
    while True:
        rps_choice = get_choices()
        pc_choice = random.choice(choices)
        show_choices(rps_choice, pc_choice)
        determine_winner(rps_choice, pc_choice)
        
        cont = input("Do you want to continue?(y/n): ").lower()
        if cont=="n":
            break
        
play_game()
