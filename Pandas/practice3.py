import pandas as pd

myData =  {
  'cars' : ["BMW","TOYOTA","FORD"],
  'passings' : [3,7,2]
}
x = pd.DataFrame(myData)
print(x)