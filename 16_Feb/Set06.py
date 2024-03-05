set1={True,1,2,3,4,5,1,2,10}
set3 = {1,"aa",True,200,10} # True is considered as 1, False is considered as 0
union_set = set1.union(set3)
print(set1)
print(union_set)

inter_set = set1.intersection(set3)
print(inter_set)

my_set = set1.difference(set3)
print(my_set)

my_set1 = set3.difference(set1)
print(my_set1)

subset = set3.issubset(set1)
print(subset)

print(set1)
set1.remove(2)
print(set1)
set1.remove(1)
print(set1)