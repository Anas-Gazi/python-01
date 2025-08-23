s= ['1','2','3','5']

def double(val):
    return val * 2
res =list (map(double,s))
print(res)

a = [1, 2, 3, 4]

# Custom function to double a number
def double(val):
    return val * 2
res = list(map(double, a))
print(res)

# output
# ['11', '22', '33', '55']
# [2, 4, 6, 8]