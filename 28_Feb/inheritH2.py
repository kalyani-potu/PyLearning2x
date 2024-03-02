class Vehicle:
    def info(self):
        return "This is vehicle"


class Car(Vehicle):
    def info(self):
        return "The car"


class Bicycle(Vehicle):
    def info(self):
        return "The Bicycle"


car_ref = Car()
print(car_ref.info())

bicycle_ref = Bicycle()
print(bicycle_ref.info())

vehicle_ref = Vehicle()
print(vehicle_ref.info())
