#polymorphism of inbuilt functions

print(len("geeks"))
print(len([10,20,30]))

#polymorphism of userdefined functions
def add(x,y,z=0):
    return x+y+z
print(add(2,3))
print(add(2,3,4))