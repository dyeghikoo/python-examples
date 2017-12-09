# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 15:50:49 2017

@author: Diego
"""

def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    minimo = min(a,b)
    maximo = max(a,b)
    if a == 0:
        return b
    elif b == 0:
        return a   
    elif a%minimo == 0 and b%minimo == 0:
        return minimo
    else:
        return(gcdRecur(minimo,maximo%minimo))