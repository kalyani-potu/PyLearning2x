def seq_num(num):
    return num ** 2


numbers = [1, 2, 3, 4, 5]
new_list = list(map(seq_num, numbers))
print(new_list)
