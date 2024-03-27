class GF:
    def __init__(self):
        self.inp = None

    def drive_car(self):
        print(self.inp, "Lambo")


class Father(GF):
    def __init__(self):
        self.inp = "FFFiNN"

class Son(Father):
    pass


pramod = Son()
#pramod.inp = "prrrr"
pramod.drive_car()

mmd = Father()
#mmd.inp = "FFFFFFF"
mmd.drive_car()

gkd = GF()
#gkd.inp = "GFGFG"
gkd.drive_car()
