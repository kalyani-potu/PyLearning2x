my_dict = {'b':2, 'a':1, 'c':3}
new_dict = my_dict.copy()
print(my_dict)
print(new_dict)
print(id(my_dict))
print(id(new_dict))

new_dict1 = my_dict
print(my_dict)
print(new_dict1)
print(id(my_dict))
print(id(new_dict1))