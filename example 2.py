# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 02:29:56 2017

@author: Diego

In this problem, you'll create a program that guesses a secret number!
The program works as follows: you (the user) thinks of an integer between 
0 (inclusive) and 100 (not inclusive). The computer makes guesses, 
and you give it input - is its guess too high or too low? 
Using bisection search, the computer will guess the user's secret number!
"""

low = 0
high = 100
number = int((low + high)/2) 
result = ""

print("Please think of a number between 0 and 100!")

while(result != 'c'):
    print("Is your secret number " + str(number) + "?")
    print("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate", end='') 
    print("the guess is too low. Enter 'c' to indicate I guessed correctly.", end=' ')
    result = input()
    if result == "h":
        high = number
        number = int((low + high)/2)       
    elif result == "l":
        low = number
        number = int((low + high)/2)        
    elif result == "c":
        break
    else:
        print("Sorry, I did not understand your input.")
print("Game over. Your secret number was: " + str(number))