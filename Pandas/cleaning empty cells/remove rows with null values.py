import pandas as pd
df = pd.read_csv(r'C:\Users\arana\OneDrive\Desktop\DSA\Pandas\new Data.csv')

df.dropna(inplace= True)
print(df.to_string)

#dropna(inplace = True) will NOT return a new DataFrame, but it will remove all rows containing NULL values from the original DataFrame.