# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 12:16:00 2018

@author: fairly_oddparents
"""

def sequence_sum(begin_number, end_number, step):
    n = 1 + (end_number-begin_number)//step
    addition = 0.5*n*(begin_number+end_number)
    return addition
   

    
    
print(sequence_sum(2, 6, 2))
#12
print(sequence_sum(-1, -5, -3))
#-5
print(sequence_sum(1, 5, 1))
#15
print(sequence_sum(1, 5, 3))
#5
print(sequence_sum(16, 15, 3))
#0
print(sequence_sum(780, 6851543, 5))
#4694363402480

