import math
def cb_rt(num):
    return math.cbrt(num)

list1 = [27,1,64]
cb_list = list(map(cb_rt, list1))
print(cb_list)