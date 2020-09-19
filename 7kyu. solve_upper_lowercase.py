# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 12:31:16 2018

@author: fairly_oddparetns
"""

def solve(s):
    count_lowercase = 0
    for character in s:
        if character.islower() == True:
            count_lowercase += 1 
    if count_lowercase >= len(s)/2:
        return s.lower()
    else:
        return s.upper()
    
print(solve("code"))
print(solve("CODe"))
print(solve("COde"))
print(solve("Code"))