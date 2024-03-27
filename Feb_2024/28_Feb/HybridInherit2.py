class A:
    def method(self):
        return "Method A"
class B(A):
    pass
   # def method(self):
    #    return "Method B"
class E:
    def method(self):
        return "Method E"
class C(E):
    pass
   #def method(self):
   #    return "Method C"
class D(B,C):
    pass
   # def method(self):
     #   return "Method D"

d=D()
print(d.method())
