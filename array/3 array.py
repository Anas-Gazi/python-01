import array as arr
a= arr.array('i', [1,2,3])

print(a[0])
a.append(5)
print(a)

#next creating ana array

import array as arr
a= arr.array('i', [2,4,1,3])


for x in range(0 ,4): 
  #print(x) #print  number in column
  #print(a) #print array('i', [1, 2, 3, 5]) 5 times 
  print(a[x], end=" ") # print 2 4 1 3
  