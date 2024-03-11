import os
print(os.getcwd())
path = 'C:\\All\\Python\\PyLearning2x\\28_Feb\\aaa.txt'
with open(path) as file : #with open(path, 'r') as file :
    print(file.read())