set1={True,1,2,3,4,5,1,2,10}
set2 = set1
print(set1)
print(set2)
print(id(set1))
print(id(set2))

set1.pop() #removes random item
print(set1)
print(set2)


