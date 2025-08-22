#Adding Elements to an Array

import array as arr
a= arr.array('i',[1,2,3])

print(*a)
a.insert(1,4)
print(*a)