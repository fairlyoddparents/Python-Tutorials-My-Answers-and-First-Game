# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 20:24:58 2018

@author: fairly_oddparents
"""

def work_needed(projectMinutes, freeLancers):
    f_hrs = 0
    f_mins = 0
    for freelancer in freeLancers: 
        f_hrs += freelancer[0]
        f_mins += freelancer[1]
    f_time = (f_hrs*60)+f_mins
    if projectMinutes-f_time>0:
        hours = (projectMinutes-f_time)//60
        minutes = (projectMinutes-f_time)%60
        return("I need to work %d hour(s) and %d minute(s)" % (hours, minutes))
    else:
        return("Easy Money!")


work_needed(600, [(3,14), (4,15), (2, 25)])