import math

def cube(num):
    return math.pow(num,3)

numbers = [5,3,9]
cube_list = list(map(cube, numbers))
print(cube_list)