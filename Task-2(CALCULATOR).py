# -*- coding: utf-8 -*-
"""
Created on Sun May 12 16:49:10 2024

@author: bhask
"""

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero!"
    else:
        return x / y

print("welcome to the world of calculations!")
print("I can perform:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

while True:
    choice = input("Enter operation choice (1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if choice == '1':
            print("Result:", add(num1, num2))
        elif choice == '2':
            print("Result:", subtract(num1, num2))
        elif choice == '3':
            print("Result:", multiply(num1, num2))
        elif choice == '4':
            print("Result:", divide(num1, num2))
        
        break
    else:
        print("Invalid input. Please enter a number between 1 and 4.")
