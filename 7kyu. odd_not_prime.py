# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 09:14:33 2018

@author: fairly_oddparents
"""

def is_prime(n):
    even = [x for x in range(n+1) if x%2 != 0]
    primes = [1,3,5]
    for num in even:
        for prime in primes:
            if num%prime != 0:
                primes.append(num)
                
    print(even)
    print(primes)
        
    
            
            

is_prime(100)