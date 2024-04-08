class Person(object): #This is same as class Person
    name = None
    age = None
    id = None

    def talk(self):
        print("I can talk")

    def walk():
        print("I can walk")

    def sleep(self):
        return "I am sleeping"


def func1(): # function independent of class
    print("I am a function - Independent of class")


kalyani = Person()
print("Name is", kalyani.name)
kalyani.name = "Kalyani Potu"
print("Name is", kalyani.name)
kalyani.talk()
#kalyani.walk() --> it gives error, because walk() didn't have self parameter, it doesn't refer to instance(object) of class
Person.walk() #direclty calling walk()
print(kalyani.sleep())
print("Name is", Person.name)
print("Name is", Person().name)
Person().talk()

func1()
