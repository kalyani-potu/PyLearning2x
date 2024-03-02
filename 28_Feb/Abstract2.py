from abc import ABC, abstractmethod


class ATB(ABC):

    @abstractmethod
    def perform_task1(self):
        pass

    @abstractmethod
    def perform_task2(self):
        pass


class Amit(ATB):
    def perform_task1(self):
        return "Bow Bow"

    def perform_task2(self):
        return "Meow Meow"


amit = Amit()
print(amit.perform_task2())
print(amit.perform_task1())