class GF:
    def __init__(self):
        self.inp = None

    def drive_car(self):
        print(self.inp, "Lambo")


class Father(GF):
    pass

class Son(Father):
    pass


pramod = Son()
print(pramod.inp)
pramod.inp = "prrrr"
pramod.drive_car()

mmd = Father()
mmd.inp = "FFFFFFF"
mmd.drive_car()

gkd = GF()
gkd.inp = "GFGFG"
gkd.drive_car()
