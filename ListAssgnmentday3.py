l = [1,4,9,10,23]
l1= l[1:3]  #get 4,9
print (l1)
l2 = l[-2:] #get 10,23
print (l2)
l.append(90) #append
print(l)
l3 = [180]
l = l + l3 #concatenate
print(l)
l4 = l.extend(l3) #concatenate using extend, note l4 is introdiced to avoid null output
print(l)

avg = sum(l)/len(l) # calculate average
print("the average is ", round(avg,2))

del l[1:3] #remove 4 & 9

print(l)