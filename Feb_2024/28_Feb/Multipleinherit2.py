class Father :
    def home(self):
        return "This is from Father"

class Mother :
    def home(self):
        return "This is from Mother"
class Daughter(Mother, Father):
    pass

D_ref= Daughter()
print(D_ref.home())