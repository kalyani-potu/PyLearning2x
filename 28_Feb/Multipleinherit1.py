class Father :
    def home(self):
        return "This is from Father"

class Mother :
    def home(self):
        return "This is from Mother"
class Daughter(Father, Mother):
    pass

D_ref= Daughter()
print(D_ref.home())