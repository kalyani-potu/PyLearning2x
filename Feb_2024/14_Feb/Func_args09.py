def fact(n):
    i = 1
    fact_var = 1
    for i in range(1, n + 1):
        fact_var = fact_var * i
    return fact_var

result = fact(int(input("Enter the number : ")))
print(result)
