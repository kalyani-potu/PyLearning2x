n = int(input('Enter the number :'))
fact = 1
if n > 0:
    #while n > 0:
    #    fact = fact * n
    #    n = n - 1
    for i in range(1,n+1):
        fact = fact * i
    print(fact)
else:
    print("Invalid input")

