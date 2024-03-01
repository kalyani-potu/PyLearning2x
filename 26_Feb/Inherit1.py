class Father:
    __private_villa = "GOA"
    gold = 5
    def drive_car(self):
        print("Lambo")

    def threeBHKFlat(self):
        print("3BHK Flat")
    def private_vill_access(self, is_my_son):
        if is_my_son :
            print(self.__private_villa)
        else :
            print("Not allowed")

class Son(Father):
    pass

pramod = Son()
print(pramod.gold)
pramod.drive_car()
pramod.threeBHKFlat()
pramod.private_vill_access(True)
#print(pramod.__private_villa) # error since this is private variable

mmd = Father()
print(mmd.gold)
mmd.drive_car()
mmd.threeBHKFlat()