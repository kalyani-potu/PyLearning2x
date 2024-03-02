class GF:
    def __init__(self, inp):
        self.GFinp = inp
    def drive_car(self):
        print(self.GFinp, "Lambo")

class Father(GF):
    pass
class Son(Father):
    pass

pramod = Son("son")
pramod.GFinp = "prrrr"
pramod.drive_car()

mmd = Father("F")
mmd.drive_car()

gkd = GF("GF")
#gkd.GFinp = "prrrr"
gkd.drive_car()
