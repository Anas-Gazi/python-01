import pandas as pd

df = pd.read_csv(r'C:\Users\arana\OneDrive\Desktop\DSA\Pandas\new Data.csv')
new_df = df.dropna()
print(new_df.to_string)

# some rows have been removed 18, 22 and 28
#These rows had cells with empty values.
#dropna() method returns a new DataFrame, and will not change the original.