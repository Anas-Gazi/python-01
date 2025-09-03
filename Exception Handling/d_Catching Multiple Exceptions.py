a= ["10","twenty",30]
try:
  total = int(a[0]) + int(a[1])

except(TypeError, ValueError) as e:
  print("Error",e)

except(IndexError):
  print("Index out of range. ")