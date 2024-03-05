def seq_num(num):
    return num ** 2


numbers = [1, 2, 3, 4, 5]
new_list = list(map(seq_num, numbers))
print(new_list)

num_tuple = (1,2,3,4,5,6)
new_tuple = tuple(map(seq_num, num_tuple))
print(new_tuple)

num_set = {1,2,3,4,5,6,7}
new_set = set(map(seq_num, num_set))
print(new_set)