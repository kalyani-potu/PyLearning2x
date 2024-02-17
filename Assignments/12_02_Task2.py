def factorial(n):
    if n>0 :
        fact = 1
        for i in range(1, n+1):
            fact = fact * i
        return fact
    else :
        return "Invalid number"


result = factorial(int(input("Enter a number:")))
print(result)
