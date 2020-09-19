# -*- coding: utf-8 -*-
"""
Editor de Spyder

created by fairly_oddparents
"""
def next_smaller(n):
    num = [int(digit) for digit in str(n)]
    lenght = len(num)-1
    for digit in num:
        if num[lenght]<num[lenght-1]:
            replacement = num[lenght]
            num[lenght] = num[lenght-1]
            num[lenght-1] = replacement
            break
        lenght -= 1
    result = ""
    for x in num:
        x = str(x)
        result += x
    return(int(result))

    
           
    
next_smaller(513)
