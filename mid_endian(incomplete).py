# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 16:15:12 2018

@author: fairly_oddparents
"""

def mid_endian(n):
    hexa = hex(n)[2:].upper()
    if len(hexa)%2 != 0:
        hexa = "0" + hexa
    lst = [hexa[i:i+2] for i in range(0, len(hexa), 2)] 
    
    first = []
    second = []
    for pair in lst:
        first.append(lst[x] for x in range(-1, -len(hexa), 2))
        second.append(lst[y] for y in range (0, len(hexa), 2))
    
    print(first)
    

mid_endian(0)
mid_endian(43135012110)
mid_endian(5446664505640567920)

#Test.assert_equals(mid_endian(9999999),"96987F")
#Test.assert_equals(mid_endian(0),"00")
#Test.assert_equals(mid_endian(658188),"0B0A0C")
#Test.assert_equals(mid_endian(168496141),"0D0B0A0C")
#Test.assert_equals(mid_endian(43135012110),"0D0B0A0C0E")
#Testing for 5446664505640567920 equal '706F82964B709D44'