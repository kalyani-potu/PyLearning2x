my_tuple = (1,2,3,4,5)
my_tuple[0]=200 #tuple is immutable
print(my_tuple)

#we cannot update tuple directly, we can first modify to list and update and then change back to tuple

new = list(my_tuple)
new[0] = True
print(tuple(new))