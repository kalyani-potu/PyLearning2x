class Car:
    color = "Red"
    model = "VX001"
    def car_details(self):
        print("Your car details are ", self.color, self.model)
        print("Your car details are ", Car.color, Car.model)
        print("Your car details are ", *Car.color, *Car.model)

car_ref = Car()
car_ref.car_details()
car_ref.color = "Pink"
car_ref.model = "BZ008"
car_ref.car_details()

#*LoginPage.username
