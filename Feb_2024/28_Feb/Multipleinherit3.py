class Father :
    def __init__(self, inp):
        print('Father input is', inp)
    def home(self):
        return "This is from Father"

class Mother :
    def __init__(self, inpm):
        print('Mother input is', inpm)
    def home(self):
        return "This is from Mother"
class Daughter(Mother,Father):
    pass

D_ref= Daughter("fff")
print(D_ref.home())
