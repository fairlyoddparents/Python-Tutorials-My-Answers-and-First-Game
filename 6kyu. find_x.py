# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 11:23:51 2018

@author: fairl
"""


def find_x(n):
    y = n*2
    add_1 =0.5*y*(y-1)
    add_2 = 0.5*n*(n-1)
    x = (add_1*n) + (add_2*y)
    print(x)

"""[1, 1],
    [2, 16],
    [3, 63],
    [9, 2025],
    [13, 6253],
    [15, 9675],
    [12, 4896]"""

find_x(1)
find_x(2) #im doing this one
find_x(3)
find_x(9)
find_x(13)
find_x(15)
print("hellods")
