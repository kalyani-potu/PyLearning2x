class Mul_param :
    name = None
    def info_mthd(self, first_name):
        print("your name is ", first_name)
        a=10
        print(a)
        print("obj name is ", self.name)

#print(a)
#print(first_name)

obj_ref = Mul_param()
obj_ref.info_mthd("Drithi")
obj_ref.name = "Krithi"
obj_ref.info_mthd("Drithi")