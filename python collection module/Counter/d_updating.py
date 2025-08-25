from collections import Counter
ctr = Counter([1,2,2])

ctr.update([2,3,3,3])
print(ctr)

# Counter Methods

# Elements()
ctr = Counter([1,2,2,3,3,3])
items = list(ctr.elements())
print(items)

#most common()
ctr = Counter([1,2,2,3,3,3])
common=ctr.most_common(2)
print(common)

# subtract()
ctr = Counter([1,2,2,3,3,3])
ctr.subtract([2,3,3])
print(ctr)
