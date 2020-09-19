# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 19:38:03 2018

@author: fairl
"""

def numericals(s):
    resp = []
    copy = ""
    response = ""
    for character in s:
        if character not in copy:
            copy += character
            resp.append("1")
        else:
            resp.append(str(int(resp[copy.rfind(character)])+1))
            copy += character       
    for num in resp:
        response += str(num)
    return response
        


print(numericals("Hello, World! It's me, JomoPipi!"))                
print(numericals("aaaaaaaaaaaaA"))