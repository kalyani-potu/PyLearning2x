my_list = [True, 1, 2.4, 8, 'kalyani']
my_list = my_list + ['eee', 'jjj']
print(my_list)

my_list2 = ['eee', 'yyyy', 0]
my_list1 = my_list + my_list2
print(my_list1)

my_list1.extend('krithi')
print(my_list1)
my_list1.extend(['jj', 9])
print(my_list1)
my_list1.extend(('zz', 10, False))
print(my_list1)
my_list1.extend({'xx', 1111, True})
print(my_list1)
