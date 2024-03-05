my_tuple = (True,1,2.4,8,'kalyani')
print("The given tuple is : ", my_tuple)


tuple2 = my_tuple
print(tuple2)
print(id(tuple2))
print(id(my_tuple))

tuple2 = my_tuple + () #  prints to same memory location
print(tuple2)
print(id(tuple2))