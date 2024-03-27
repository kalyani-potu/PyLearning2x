try :
    a = int(input("Enter num1: "))
    b = int(input("Enter num2: "))
    c = a/b
    print("Div is", c)
except ZeroDivisionError as e:
    print(e)
    print("number cannot be divided by zero")
except ValueError as v:
    print(v)
print("Important message")