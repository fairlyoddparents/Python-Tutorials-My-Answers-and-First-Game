# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 11:15:59 2018

@author: fairly_oddparents
"""

def square_up(n):
    result = []
    lst = [x*0 for x in range(n)]
    i = -1
    j = 1
    for z in range(n):
        lst[i] = j
        result += lst       
        i -= 1
        j += 1    
    return result
    
    
    
    
print(square_up(4))
