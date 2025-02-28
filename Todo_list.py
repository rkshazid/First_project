# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 22:10:51 2025

@author: shazi
"""

import sys

tasks = []
def add_task(task):
    tasks.append(task)
    print(f'Task "{task}" added.')
    
def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        print(f'Task "{task}" removed.')
    else:
        print(f'Task "{task}" not found.')
        
def view_task():
    if tasks:
        for i, task in enumerate(tasks, start=1):
            print(f'{i}. {task}')
    else:
        print("No tasks available")

def show_menu():
    print("\nTo-Do List")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. View Task")
    print("4. Exit")
    
def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1/2/3/4): ")
        if choice == "1":
            task = input("Enter the task to add: ")
            add_task(task)
        elif choice == "2":
            task = input("Enter the task to remove: ")
            remove_task(task)
        elif choice == "3":
            view_task()
        elif choice == "4":
            sys.exit()
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
