# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 13:41:32 2017
Implement the function isIn(char, aStr) which implements the above 
idea recursively to test if char is in aStr. char will be a 
single character and aStr will be a string that is in alphabetical order. The function should return a boolean value.
@author: Diego
"""

char = 'a'
aStr = ''

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    if len(aStr) <= 1:
        if char == aStr:
            return True
        else:
            return False
    elif char == aStr[round(len(aStr)/2)-1]:
        return True
    elif ord(char) < ord(aStr[round(len(aStr)/2)-1]):
        return isIn(char, aStr[:round(len(aStr)/2)-1])
    elif ord(char) > ord(aStr[round(len(aStr)/2)-1]):
        return isIn(char, aStr[round(len(aStr)/2):])

print(isIn(char,aStr))