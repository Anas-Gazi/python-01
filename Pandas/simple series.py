import pandas as pd

a= [7,8,9]
x= pd.Series(a, index=['x','y','z',]) #with index argument  i can use my own index
print(x)