class XYZ:
    def f1(self):
        try :
            a = int(input("Enter a number : "))
        except Exception as e :
            print("Enter integer only for value of a")
        else :
            print(a)
        finally :
            print("Anyhow I will be printed")
x = XYZ()
x.f1()