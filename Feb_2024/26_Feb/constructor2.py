class Car:
    name = None
    model = None
    make = None

    def __init__(self, o_name = 'D_car', o_model= 'D_model', o_make = '1111'):  # constructor
        self.name = o_name
        self.model = o_model
        self.make = o_make

    def start_engine(self):
        print("car name is " + self.name)
        print("car model is " + self.model)
        print("car make is " + self.make)


lambo = Car() #error--> when there are no default values for arguments,  if argument values are not passed while object creation, it gives error
lambo.start_engine()

