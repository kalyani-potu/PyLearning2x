from abc import ABC, abstractmethod
class Animal(ABC):
    def __init__(self, name):
        self.name=name

    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "bow bow"

class Cat(Animal):
    def sound(self):
        return "Meow "

dog=Dog("dd")
print(dog.sound())

cat=Cat("CC")
print(cat.sound())