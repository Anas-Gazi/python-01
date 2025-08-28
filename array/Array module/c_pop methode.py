import array

arr = array.array('i',[1,2,3,4,5])
for i in range(0,5):
  print(arr[i],end=" ")

print('\r')

print(arr.pop(2))# removes 3, prints 3

for i in range(len(arr)):
  print(arr[i], end=" ")