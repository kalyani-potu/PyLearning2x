class Animal:
    def __init__(self):
        pass
    def sound(self):
        print("Animal Sound")
    def ani_mthd(self):
        print("Animal method")

class Dog(Animal):
    def __init__(self):
        pass
    def sound(self):
        super().sound()
        super().ani_mthd()
        print("Dog Sound")

dog = Dog()
dog.sound()

ani = Animal()
ani.sound()