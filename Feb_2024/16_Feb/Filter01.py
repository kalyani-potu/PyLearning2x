numbers = [1,2,3,4,5,6,7]
even_numbers = filter(lambda number : number % 2==0, numbers)
print(list(even_numbers))


#######################################
numbers = [1,2,3,4,5,6,7]
def even(num):
    return num%2==0 # returns either true or flase
even_numbers1 = filter(even, numbers)
print(list(even_numbers1))