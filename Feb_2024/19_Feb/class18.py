class Car:
    n = "100"
    def car_details(self):
        print("Your car details are ", self.n)
        print("Your car details are ", Car.n)

        print("Your car details are ", *Car.n)

car_ref = Car()
print(Car.n)
car_ref.car_details()
car_ref.n = 150
print(Car.n)
car_ref.car_details()