with open("kalyani.txt", 'a') as file:
    file.write("\n Hello Drithix, How are you ?")

with open("kalyani.txt", 'r') as file:
    line = file.readline()
    print(line)
file.close()

with open("kalyani.txt", 'r') as file:
    line = file.readlines()
    print(line)
file.close()