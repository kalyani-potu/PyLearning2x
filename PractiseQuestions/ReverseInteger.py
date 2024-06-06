num = int(input("Enter the number :"))
result = 0
while num > 0:
    r = num % 10
    result = result * 10 + r
    num = num // 10
print(result)
