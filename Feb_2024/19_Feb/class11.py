class Car:
    name = None
    color = None
    model = None
    speed = None
    engine = None

    def start_engine(self):
        print("starting engine")

    def drive(self):
        print("Drive")

    def car_break(self):
        print("Break")

    def who_is_driving(self):
        print("I am driving " + self.name)


tesla_obj = Car()
lambo_obj = Car()

tesla_obj.name = "Tesla"
lambo_obj.name = "Lambo"

tesla_obj.who_is_driving()
lambo_obj.who_is_driving()
