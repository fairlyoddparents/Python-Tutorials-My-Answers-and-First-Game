# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 21:41:21 2018

@author: fairly_oddparents
"""

def remove_rotten(bag_of_fruits):
    fresh_fruit = []
    if bag_of_fruits != None: 
        for fruit in bag_of_fruits:
            if fruit.startswith("rotten"):
                fresh_fruit.append(fruit[6:].lower())
            else:
                fresh_fruit.append(fruit)
    return(fresh_fruit)

remove_rotten(["apple","rottenBanana","apple"])