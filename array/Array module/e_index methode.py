import array
arr= array.array('i',[1,2,3,4,5])
for i in range(0,5):
  print(arr[i], end=" ")

print("\r")
# using index() to print index of 1st occurrence of 2
print(arr.index(2))