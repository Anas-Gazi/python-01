import array

arr= array.array('i',[1,2,3])
print("The new created array is:\n", end="")
for i in range(0,3):
  print(arr[i], end="")
  print("\r")

arr.append(4)
print("The append array is:\n",end="")
for i in range(len(arr)):
  print(arr[i],end=" ")

