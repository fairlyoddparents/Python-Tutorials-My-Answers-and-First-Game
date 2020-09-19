# -*- coding: utf-8 -*-
"""
Created on Sun Jul 29 14:45:35 2018

@author: fairly_oddparents
"""

def wave(text):
    result = []
    for i in range(len(text)):
        waved = ""
        for j, letter in enumerate(text):
            if j == i:
                waved += letter.upper()
            else: 
                waved += letter
        if waved.islower() == False:
            result.append(waved)
    return result
    

print(wave("hell"))



        
        
 