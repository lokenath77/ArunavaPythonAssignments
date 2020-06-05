# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 01:26:27 2020

@author: AD5023775
"""

ages = {
"Peter": 10,
"Isabel": 11,
"Anna": 9,
"Thomas": 10,
"Bob": 10,
"Joseph": 11,
"Maria": 12,
"Gabriel": 10,
}

def convert(ages,n):
    for kk,vv in ages.items():
        ages.update({kk:vv+int(n)})
    print('this is the new dict:',ages)
        
        
n = input("enter increment value :")        
convert(ages,n)