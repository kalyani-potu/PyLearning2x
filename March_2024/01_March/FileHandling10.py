with open("kalyani.txt", 'r') as file:
    lines = file.readlines()
    print(lines)
for line in lines :
    print(line, end = '')
file.close()