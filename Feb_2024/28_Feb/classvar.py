class A:
    name = "name"
    def methd(self):
        self.name = 'aaaa'
        print(1111)


a_ref = A()
print(a_ref.name)
a_ref.name = 'sss'
a_ref.methd()
print(a_ref.name)

a2_ref=A()
print(a2_ref.name)