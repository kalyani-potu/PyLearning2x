a = float(input('Enter first side :'))
b = float(input('Enter second side :'))
c = float(input('Enter third side :'))
if a > 0 and b > 0 and c > 0:
    if a == b == c:
        print('Equilateral Triangle')
    #elif a == b != c or a != b == c or a == c != b:
    elif a == b or b == c or a == c:
        print('Isosceles Triangle')
    else:
        print('Scalene Triangle')
else:
    print('Invalid input')
