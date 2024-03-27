def sum_num(a, b): # returntype with args
    return a + b


result = sum_num(3, 4)
result1 = sum_num("Kalyani", "Potu")
result2 = sum_num(a=3, b=4)  # we can pass like this if we know the variable names used in args
# result3 = sum_num("Kalyani", 32) # addition of string and int gives error
print(result)
print(result1)
print(result2)
# print(result3)
