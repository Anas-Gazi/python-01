import pandas as pd

data= {
  'calories': [400,500,650],
  'duration':[40,50,60]
}

x=pd.DataFrame(data)
print(x.loc[[0,1]])