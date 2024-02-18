def f1(a=1,b=2,c=3):
    return a+b+c


result = f1()
result1 = f1(4)
result2 = f1(4,5)
result3 = f1(4,5,6)
result4 = f1(a=10,b=20,c=30)
result5 = f1(c=40,a=50,b=10) #For best practises, always recommended to assign them in the order
print(result)
print(result1)
print(result2)
print(result3)
print(result4)
print(result5)