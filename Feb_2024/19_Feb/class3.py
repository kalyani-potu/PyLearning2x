class Person:
    name = None
    age = None
    id = None

    def talk(self, name):
        print(f"{name} can talk")

    def walk(self):
        print("I can walk")

    def sleep(self):
        return "I am sleeping"


kalyani = Person()
kalyani.name = "Kalyani Potu"
print("Name is", kalyani.name)
kalyani.talk("Kalyani")
kalyani.walk()
print(kalyani.sleep())

drithi = Person()
drithi.name = "Drithi P"
print("Name is", drithi.name)
drithi.talk("Drithi")
drithi.walk()
print(drithi.sleep())