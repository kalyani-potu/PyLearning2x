def sum_num(a, b, c, d, e):
    return a + b + c + d + e


result = sum_num(1, 2, 3, 4, 5)
print(result)


# With args and for loop
def sum_args(*args):  # args ==> we can pass any number of values
    sum1 = 0
    for i in args:
        sum1 = sum1 + i
    return sum1


result = sum_args(10, 20, 100, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
print(result)
