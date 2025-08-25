from collections import Counter

ctr1 = Counter([1,2,2,3])
ctr2 = Counter([2,3,3,4])

#addition
print(ctr1 + ctr2)
#subtraction
print(ctr1 - ctr2)
#Intersection
print(ctr1 & ctr2)
#Union
print(ctr1 | ctr2)

