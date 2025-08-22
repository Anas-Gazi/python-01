from functools import reduce

def add(x,y):
  return x+y
a=[1,2,3,4,5,6,4]
ref= reduce(add,a)
print(ref)

#Common Use Cases of reduce()
#Summing all numbers in a list.
# Multiplying elements for a factorial.
# Finding maximum or minimum in a sequence.
# Concatenating strings.
# Flattening nested lists.