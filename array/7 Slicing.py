import array as arr
a= [1,2,3,4,5,6,7,8,9,10]
b= arr.array('i',a)

res = a[3:5] #start from next, end on given last
print(res)

res= a[:5]
print(res)

res= a[5:]
print(res)

res =a[:]
print(res)

res =a[:-5]
print(res)