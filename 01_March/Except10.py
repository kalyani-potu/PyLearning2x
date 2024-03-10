try:
    a = int(input("Enter a number only \n"))
except ValueError as v :
    print(v)
except Exception as e:
    print(e)
else:
    print("else")