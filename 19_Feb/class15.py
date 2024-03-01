class Car:
    color = None
    model = None
    def car_details(self):
        print("Your car details are ", self.color, self.model)

car_color = input("Enter your car color :")
car_model = input("Enter your car model :")

car_ref = Car()
car_ref.color = car_color
car_ref.model = car_model

car_ref.car_details()
