# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 21:11:23 2017

@author: Diego

Assume s is a string of lower case characters.
Write a program that prints the longest substring of s in which the letters 
occur in alphabetical order. For example, if s = 'azcbobobegghakl', 
then your program should print:
Longest substring in alphabetical order is: beggh
In the case of ties, print the first substring. For example, 
if s = 'abcbcd', then your program should print:
Longest substring in alphabetical order is: abc
"""


s = 'uriomfcjlt'
ABC = "abcdefghijklmnopqrstuvwxyz"
posicionActual = 0
posicionAnterior = 0
cadena = ""
cadenaFinal = ""
contador = 0

for letra in s:
    for abcdario in ABC:
        if letra == abcdario:
            posicionActual = contador
        else:
            contador += 1
    contador = 0
    if posicionActual >= posicionAnterior:
        cadena += letra
    else:
        if len(cadena) > len(cadenaFinal):
            cadenaFinal = cadena
        cadena = letra 
    posicionAnterior = posicionActual
    posicionActual = 0
if len(cadena) > len(cadenaFinal):
    cadenaFinal = cadena            
print("Longest substring in alphabetical order is: " + cadenaFinal)