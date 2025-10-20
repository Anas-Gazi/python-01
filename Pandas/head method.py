import pandas as pd
x = pd.read_csv(r'C:\Users\arana\OneDrive\Desktop\DSA\Pandas\data.csv')
print(x.head(10))
#this will print first 10 rows
print(x.head())

#and if you skip 10 or don't use any number,  head() will print only first 5 rows