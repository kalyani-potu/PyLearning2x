a = 5
b = 5
c = 10
list1 = []
list2 = []
list3 = list1
print('1 : ', a == b)  # numbering just for order
print('2 : ', a == c)
print('3 : ', a is b)
print('4 : ', a is c)
print('5 : ', list1 == list2)
print('6 : ', list1 is list2)
print('7 : ', list3 is list1)
list3 = list3 + list1
print('8 : ', list3 is list1)
print(list3)
