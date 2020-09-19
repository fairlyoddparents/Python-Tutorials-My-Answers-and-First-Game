# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 19:05:20 2018

@author: fairly_oddparents
"""

def communication_module(packet):
    response = 0
    num1 = int(packet[8:12])
    num2 = int(packet[12:16])
    inst = packet[4:8]
    if inst == "0F12":
        response += (num1+num2)
    elif inst == "B7A2":
        response += (num1-num2)
    else:
        response += (num1*num2)
    if response < 0:
        response = 0
    if response > 9999:
        response = 9999
    return "%sFFFF%04d0000%s" % (packet[0:4], response, packet[16:20])
  

print(communication_module("X7X7B7A201400058L0L0"))
    