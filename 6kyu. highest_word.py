# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 11:16:47 2018

@author: fairly_oddparents
"""
alphabet = {"a":1, "b":2, "c":3, "d":4, "e":5, "f":6,
            "g":7, "h":8, "i":9, "j":10, "k":11, "l":12,
            "m":13, "n":14, "o":15, "p":16, "q":17, "r":18,
            "s":19, "t":20, "u":21, "v":22, "w":23, "x":24,
            "y":25, "z":26}

def highest_score(text):
    text = text.split()
    single_score = 0
    scores = []

    for term in text:
        for letter in term:
            if letter in alphabet:
                single_score += alphabet[letter]
        scores.append(single_score)
        single_score=0
    sorted_scores = sorted(scores)
    highest = sorted_scores[-1]
    result = text[scores.index(highest)]
    print(result)

highest_score("taxi what time are we climbing up the volcano")
