#Methodoverriding
class Bird:
    def intro(self):
        print("There are many types of birds")
    def flight(self):
        print("few birds fly and few can't")

class Sparrow(Bird):
    def flight(self):
        print("sparrows can fly")

class Ostrich(Bird):
    def flight(self):
        print("ostrich cannot fly")

obj_bird=Bird()
obj_spr=Sparrow()
obj_ost=Ostrich()

obj_bird.intro()
obj_bird.flight()

obj_spr.intro()
obj_spr.flight()

obj_ost.intro()
obj_ost.flight()