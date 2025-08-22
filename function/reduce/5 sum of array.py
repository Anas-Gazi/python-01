from itertools import accumulate
from operator import add

a=[1,2,3,4,5,6,7]
res=accumulate(a,add)
print(list(res))