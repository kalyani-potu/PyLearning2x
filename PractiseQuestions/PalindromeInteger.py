num = int(input("Enter the number :"))
result = 0
num1=num
while num > 0:
    r = num % 10
    result = result * 10 + r
    num = num // 10
print(result)

if num1 == result:
    print("Given integer is a palindrome")
else:
    print("Given integer is not a palindrome")