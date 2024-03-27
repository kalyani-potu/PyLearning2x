num1 = input("enter first number :") # input() by default returns string value
num2 = input("enter second number :")
print(type(num1))
sum = num1 + num2
print(sum) # gives string value as num1 and num2 are not converted to int
sum = int(num1) + int(num2)
print("sum is", sum)