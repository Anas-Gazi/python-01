import pandas as pd
x= pd.read_csv(r'C:\Users\arana\OneDrive\Desktop\DSA\Pandas\data.csv')
pd.options.display.max_rows = 9999 #it will increase the mximum number of rows to display the entire data frame. 
print(x)

# why i should use this??
#if you don't use this, print(x) will return only 1st and last 5 rows