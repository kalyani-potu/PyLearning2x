class MathUtil :
    def add(self,a,b=0,c=0):
        return a+b+c
math = MathUtil()
print(math.add(1))
print(math.add(1,2))
print(math.add(1,2,3))