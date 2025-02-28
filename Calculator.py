# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 23:07:27 2025

@author: shazi
"""

def calculator():
    print("Basic Calculator")
    
    # Get the user input
    num1 = float(input("Type your 1st number: "))
    num2 = float(input("Type your 2nd number: "))
    operation = input("Choose your operation (+, -, *, /): ")
    
    # Perform Calculation
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 == 0:
            print("Error: Division by zero is invalid")
            return 
        result = num1 / num2
    else:
        print("Invalid operation")
        return 
    
    print(f'Result: {result}')

#Run the calculator
calculator()