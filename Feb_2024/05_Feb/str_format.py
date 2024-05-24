name = "kalyani"
age = 32
print("My name is {name}, age is {age}")
print(f"My name is {name}, age is {age}")  # f prints the variable value when variable name is given in print()
print("My name is {}, age is {}".format(name, age))
print("My name is %s, age is %d" % (name, age))

str_num = "12"
#str_num = "12a" #gives error as it contains character
int_num = int(str_num)
print(type(int_num))
print(int_num)
print(str_num)