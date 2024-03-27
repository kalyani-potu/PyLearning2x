with open("kalyani.txt", 'r') as file:
    print(file.readline(10)) #reading first 10 characters
    print(file.readline())
    print(file.readlines())

file.close()