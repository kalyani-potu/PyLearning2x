my_list = [True,1,2.4,8,'kalyani']
my_list2 = my_list.copy() # creating a copy
print(my_list2)
my_list2.append(5)
print(my_list2)
print(my_list)

#
# my_list3=my_list is not creating a copy, its another variable referring to same list
my_list3=my_list #my_list3 and my_list points to same elements,
print(my_list3)
my_list3.append(10)#append --> adds element to my_list and my_list3, it doen't create separate new list, so, my_list also have same elements
print(my_list3)
print(my_list)
print(id(my_list3))
print(id(my_list))

my_list3 = my_list3 + [12]
print(my_list3) # my_list3 is a new list
print(my_list)
print(id(my_list3))
print(id(my_list))