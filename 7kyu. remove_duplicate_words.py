# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 22:24:13 2018

@author: fairly_oddparents
"""

def remove_duplicate_words(s):
    cleaned = []
    s = s.split()
    for word in s:
        if word not in cleaned:
            cleaned.append(word)
    print(" ".join(cleaned))
    

