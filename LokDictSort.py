# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 18:57:01 2020

@author: AD5023775
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 03:50:37 2020

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

print ("the dictionary has",\
    len(ages), "entries in it")

l = list(ages.items())
#print(l)
print(type(l))
def Sort(l):
    l.sort(key = lambda x: x[1],reverse = True)
    return l

sorted_list = Sort(l)
print(type(sorted_list))
print('oldest student :',sorted_list[0])
print('youngest student :',sorted_list[7])

m= min(Sort(l))
print('youngest student:',m[0])
x= max(Sort(l))
print('oldest student :',x[0])
#print(sum(m[1]))
#avg = sum(m[1])/len(m[1])

print (ages.items())
#print('average age :',avg)

total_age = 0
total_student = 0

for value in ages.values():
   total_age += value
   total_student += 1
    
average = total_age/total_student
#
print("the average age is " + str(round(average,2)))