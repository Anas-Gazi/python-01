import numpy as np
arr = np.array([-1.1, 2.1, 3.1, 4.1, 5.1, 0.0])
x= arr.view()
arr[0]= 6.6
newarr= arr.astype(bool)
print(arr)
print(newarr)
print(arr.dtype)
print(newarr.dtype)
print(x)

