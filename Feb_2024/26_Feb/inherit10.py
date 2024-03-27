class GF:
    def home(self):
        print("5BHK")

class Father(GF):
    def home2(self):
        print("Father Home")
class Son(Father):
    def home3(self):
        print("son's home")

pramod = Son()
pramod.home()
pramod.home2()
pramod.home3()

mmd = Father()
mmd.home()
mmd.home2()

gkd = GF()
gkd.home()
