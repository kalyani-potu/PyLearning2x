class Vehicle:
    def info(self):
       return "This is vehicle"
    def newfunc(self):
        return "This is vehicle func"
class Car(Vehicle):
    def info(self):
        return "The car"

car_ref= Car()
print(car_ref.info())
print(car_ref.newfunc())