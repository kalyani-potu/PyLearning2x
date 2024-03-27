import math
def sq_rt(num):
    return math.sqrt(num)

list1 = [21,34,54]
sq_list = list(map(sq_rt, list1))
print(sq_list)