from functools import reduce

a= [1,2,3,4,5]
ref=reduce(lambda x,y: x+y, a)
print(ref)