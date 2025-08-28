import array
arr = array.array('i',[1,2,3])
for i in range(0,3):
  print(arr[i],end=" ")
arr.insert(2,5)
print("\r")
for i in range(len(arr)):
  print(arr[i], end=" ")