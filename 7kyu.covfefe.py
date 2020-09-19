# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 14:38:55 2018

@author: fairly_oddparents
"""

def covfefe(s):
    if "coverage" not in s:
        s += " "+ "covfefe"
    s = s.replace("coverage", "covfefe")
    return s


print(covfefe("nothing"))
