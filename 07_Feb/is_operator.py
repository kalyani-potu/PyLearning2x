a=5
b=5
c=10
list1 = []
list2 =[]
list3 = list1
print(a==b)
print(a==c)
print(a is b)
print(a is c)
print(list1==list2)
print(list1 is list2)
print(list3 is list1)
list3 = list3 +list1
print(list3 is list1)
print(list3)

