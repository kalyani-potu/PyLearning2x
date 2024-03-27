class Person:
    name = None
    age = None
    id = None

    def talk(self):
        print("I can talk")

    def walk(self):
        print("I can walk")

    def sleep(self):
        return "I am sleeping"


def func1(): # function independent of class
    print("I am a function - Independent of class")


kalyani = Person()
kalyani.name = "Kalyani Potu"
print("Name is", kalyani.name)
kalyani.talk()
kalyani.walk()
print(kalyani.sleep())

func1()
