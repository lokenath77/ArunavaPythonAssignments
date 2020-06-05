# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 23:46:30 2020

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

"""
def my_function(name,age):
    studname = name
    studage = age
    
    
my_function(**ages)

"""

l = list(ages.items())
print(l)
#x=[1,2,3,4,5] 

#print(new_list) 

#print(l)
#print(type(l))
def Convert2(l,n):
    new_list=[(i,(value + int(n))) for i,value in l]
    print('this is the new list',new_list)
    it = iter(new_list)
    res_dct = dict(zip(it,it))
    print ('new dictionary of ages :',res_dct)
    #print('new list is now ',new_list)
    #return(new_list)
"""
def Convert(l,n):
    New_list = l
    for i,value in l:
        print('value is now :',value)
        print('value of n is now :',n)
        print('vlue of i is ', i)
        value += int(n)
        print('New val is now :',value)
       # New_list = New_list.append(value)
        #int(i) += 1
        #print(New_list)
        #how to include new values in the list ?
    return(l)
    """
n= input('enter increment value :')

#def ConvertListDict(New_list):


Convert2(l,n)

#ConvertListDict(New_list)
#print('New list', new_list)
#How to convert this into a dictionary

