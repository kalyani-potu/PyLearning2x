import math

num = int(input("Enter a number :"))
sq = math.pow(num, 2)  # pow() returns float
cb = math.pow(num, 3)
print("square of a number is ", sq)
print("cube of a number is ", cb)
sq1 = float(num ** 2)
cb1 = num ** 3  # as num is int, it returns int
print("square of a number is ", sq1)
print("cube of a number is ", cb1)
