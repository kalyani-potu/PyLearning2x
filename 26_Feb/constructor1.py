class Car:
    name = None
    model = None
    make = None

    def __init__(self, o_name, o_model, o_make):  # constructor
        self.name = o_name
        self.model = o_model
        self.make = o_make

    def start_engine(self):
        print("car name is " + self.name)
        print("car model is " + self.model)
        print("car make is " + self.make)


lambo = Car('Lambo', 'L23', '2019')
lambo.start_engine()
print('------------------------------')
tesla = Car('Tesla', 'T45', '2023')
tesla.start_engine()
print('------------------------------')
XUV = Car('XUV', 'X89', '2020')
XUV.start_engine()
