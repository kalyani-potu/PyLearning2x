my_list = [9,8,9.9,9.0,1.2,1,4]
print("The given list is : ", my_list)
print(id(my_list))
my_list.sort()
print("The sorted list is : ", my_list)
print(id(my_list))

my_list = [9,8,9.9,9.0,1.2,1,4] #whenever new list is created, even if the name is same, it always stores in new memory location
print(id(my_list))

my_list = ['a','h','k','b']
print("The given list is : ", my_list)
print(id(my_list))
my_list.sort()
print("The sorted list is : ", my_list)
print(id(my_list))

my_list2 = [1,4,0]
print("The given list2 is : ", my_list2)
print(id(my_list2))
my_list2 = my_list2 +[] #even when empty list is added, it creates a new list in new memory
print("The given list2 is : ", my_list2)
print(id(my_list2))

my_list3=my_list2 # here list3 is also refering to elements of list2, so both lists points to same memory address
print("The given list3 is : ", my_list3)
print(id(my_list3))