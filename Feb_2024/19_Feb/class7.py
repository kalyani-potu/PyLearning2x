class new :
    name = None

    def mthd(self):
        print('My name is', self.name)

new_ref = new()
new_ref.name = "Kalyani"
new_ref.mthd()

new_ref2 = new()
new_ref2.name = "Drithi"
new_ref2.mthd()