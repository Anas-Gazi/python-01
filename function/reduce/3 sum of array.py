import functools 
import operator

a=[1,2,3,4,5,6,4]

print(functools.reduce(operator.add,a))
print(functools.reduce(operator.mul,a))
print(functools.reduce(operator.add,["Ami ","Valo "]))