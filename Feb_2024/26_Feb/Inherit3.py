class Father:
    def __init__(self, father_villa, f_gold):
        self.__private_villa = father_villa
        self.gold = f_gold
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
    son_home = "hyd"
    def son_car(self):
        print("son car drive")


pramod = Son("GGG", 15)
print(pramod.gold)
pramod.drive_car()
pramod.threeBHKFlat()
pramod.private_vill_access(True)
pramod.son_car()
print(pramod.son_home)
#print(pramod.__private_villa) # error since this is private variable

mmd = Father("GOA", 5)
print(mmd.gold)
mmd.drive_car()
mmd.threeBHKFlat()
