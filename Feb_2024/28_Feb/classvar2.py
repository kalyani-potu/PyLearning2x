class A:
    name = "name"
    def methd(self):
        print(1111)

class B:
    print(A.name)
    A.methd(self=A)

