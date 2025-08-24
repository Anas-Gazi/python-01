a= [x for x in range(10)]
print(a)

#nested loop
a=[(x,y) for x in range(3) for y in range(3)]
print(a)

#combine nested list in 1 list

a=[[1,2,3],[9,9,9],[6,7,8]]

res=[x for row in a for x in row]
print(res)