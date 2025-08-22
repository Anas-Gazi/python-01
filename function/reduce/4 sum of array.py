from functools import reduce

a=[1,2,3]
res= reduce(lambda x,y: x+y,a,10)
print(res)
#This code uses reduce() with a lambda function and an initial value to sum a list, starting from a given number.