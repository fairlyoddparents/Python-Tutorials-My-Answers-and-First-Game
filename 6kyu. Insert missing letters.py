# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 12:47:43 2018

@author: fairl
"""

def insert_missing_letters(text):
    text = text.upper()
    copy = ""
    alphabeth = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    reduced_alphabeth = ""
    modified = ""
    for letter in alphabeth: 
        if letter in text:
            reduced_alphabeth += " "
        if letter not in text: 
            reduced_alphabeth += letter
    for letter in text: 
        modified += letter.lower()
        if letter not in copy: 
            i = alphabeth.find(letter) + 1
            modified += reduced_alphabeth[i:]
        copy += letter         
    return modified.replace(" ", "")

print(insert_missing_letters("hello"))

