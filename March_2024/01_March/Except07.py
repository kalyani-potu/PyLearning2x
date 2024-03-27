a = int(input("Enter num1: "))
b = int(input("Enter num2: "))
try :
    c = a/b
    print("Div is", c)
except Exception as e: #when we don't know what type of exception , we can use Exception class
    print(e)
print("Important message")