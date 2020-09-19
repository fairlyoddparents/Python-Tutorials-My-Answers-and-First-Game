# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 12:56:07 2018

@author: fairl
"""

def binary_array_to_number(arr):
    decimal = 0
    for num in arr:
        decimal = decimal*2 + int(num)
        print(decimal)
    print(decimal)
    
binary_array_to_number([1,1,1,1,0,1,1])