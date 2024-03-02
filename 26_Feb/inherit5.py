class GF:
    def drive_car(self):
        print("Lambo")

class Father(GF):
    pass
class Son(Father):
    pass

pramod = Son()
pramod.drive_car()

mmd = Father()
mmd.drive_car()

gkd = GF()
gkd.drive_car()
