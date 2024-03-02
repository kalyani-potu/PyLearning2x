class GF:
    def drive_car(self, inp):
        print(inp, "Lambo")

class Father(GF):
    pass
class Son(Father):
    pass

pramod = Son()
pramod.drive_car("son")

mmd = Father()
mmd.drive_car("F")

gkd = GF()
gkd.drive_car("GF")
