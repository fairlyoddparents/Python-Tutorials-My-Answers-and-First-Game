# -*- coding: utf-8 -*-
"""
Created on Sun Jul 29 11:52:18 2018

@author: fairly_oddparents 
"""

def read_csv(txt):
    f = open(txt, "r")
    string_list = f.read().split("\n")
    
    string_fields = []
    final_list = []
    
    for line in string_list[1:]:
        row = line.split(",")
        string_fields.append(row)
        int_fields = []
        for num in row:
            int_fields.append(int(num))
        final_list.append(int_fields)
    return final_list

cdc_list = read_csv("US_births_1994-2003_CDC_NCHS.csv")
cdc_list[0:10]
# [[1994, 1, 1, 6, 8096],
# [1994, 1, 2, 7, 7772],
# [1994, 1, 3, 1, 10142],
# [1994, 1, 4, 2, 11248],
# [1994, 1, 5, 3, 11053],
# [1994, 1, 6, 4, 11406],
# [1994, 1, 7, 5, 11251],
# [1994, 1, 8, 6, 8653],
# [1994, 1, 9, 7, 7910],
# [1994, 1, 10, 1, 10498]]

def cal_counts(data, column):
    num_births = {}
    for line in data:
        if line[column] in num_births:
            num_births[line[column]] += line[4]
        else:
            num_births[line[column]] = line[4]
    return num_births

cdc_year_births = cal_counts(cdc_list, 0)
cdc_month_births = cal_counts(cdc_list, 1)
cdc_dom_births = cal_counts(cdc_list, 2)
cdc_dow_births = cal_counts(cdc_list, 3)
#{1: 5789166, 2: 6446196, 3: 6322855, 4: 6288429, 5: 6233657, 6: 4562111, 7: 4079723}

def maximum(lst):
    highest = max([i for i in lst.values()]) 
    return highest

def minimum(lst):
    lowest = min([i for i in lst.values()])
    return lowest

print("max", maximum(cdc_year_births))
print("min", minimum(cdc_year_births))
#max 4089950
#min 3880894

from collections import OrderedDict
def sorting(lst, value1, value2):
    sorted_lst = OrderedDict(sorted(lst.items()))
    return sorted_lst[1994]

print(sorting(cdc_year_births, 1996, 1998))
#3952767


