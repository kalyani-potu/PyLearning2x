class Student:
    name = None
    id = None
    batch = None

    def attend_class(self, name):
        print(f"{name} is attending class")

    def complete_assign(self):
        print("I completed assignments")

    def learn_coding(self):
        return "I am learning python"


kalyani = Student()
kalyani.name = "Kalyani Potu"
kalyani.id = 123
kalyani.batch = "Py2x"
print("Name is", kalyani.name)
print("Id is", kalyani.id)
print("Batch is", kalyani.batch)
kalyani.attend_class("kalyani")
kalyani.complete_assign()
print(kalyani.learn_coding())

krithi = Student()
krithi.name = "Krithi P"
krithi.id = 12345
krithi.batch = "Py2x"
print("Name is", krithi.name)
print("Id is", krithi.id)
print("Batch is", krithi.batch)
krithi.attend_class("krithi")
krithi.complete_assign()
print(krithi.learn_coding())