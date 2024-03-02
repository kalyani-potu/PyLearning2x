class Vehicle:
    def info(self):
        return "This is vehicle"
    def veh_mthd(self):
        return "vehh_mthd"

class Car(Vehicle):
    def info(self):
        return "The car"
    def car_mthd(self):
        return "carr_mthd"


class Bicycle(Vehicle):
    def info(self):
        return "The Bicycle"

    def Bi_mthd(self):
        return "Bic_mthd"


car_ref = Car()
print(car_ref.info())
print(car_ref.veh_mthd())
print(car_ref.car_mthd())

bicycle_ref = Bicycle()
print(bicycle_ref.info())
print(bicycle_ref.veh_mthd())
print(bicycle_ref.Bi_mthd())

vehicle_ref = Vehicle()
print(vehicle_ref.info())
print(vehicle_ref.veh_mthd())
