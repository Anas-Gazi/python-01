import numpy as np

arr = np.array([1, 2, 3, 4, 5])
#copy() 
x = arr.copy()
arr[0] = 42

print(arr)
print(x)

#view()
y = arr.view()
arr[0] = 42

print(arr)
print(y)

# [42  2  3  4  5]   after change copy 
# [1 2 3 4 5]        orginal value renaib same
# [42  2  3  4  5]   changed orginal also
# [42  2  3  4  5]
#basic difference copy can not change orginal value but view can change orginal value.see this output 