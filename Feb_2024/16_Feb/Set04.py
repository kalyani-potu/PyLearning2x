set1={True,1,2,3,4,5,1,2,10}
set1.add('kalyani') # this element can be added anywhere in the set, when each time you run the code
print(set1)

set1.remove(1)
print(set1)

set2=set1.copy() # creating a copy
print(set2)

set1.pop()
print(set1)
print(set2)
