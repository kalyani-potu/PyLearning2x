class Calculator :
    def sum(self, a=0,b=0):
        return a+b
    def sub(self, a=0,b=0):
        return a-b
    def mul(self, a=0,b=0):
        return a*b
    def div(self, a=0,b=0):
        return a/b

obj_ref= Calculator()
result = obj_ref.sum(3,4)
print("Sum is ", result)
result1 = obj_ref.sub(4,5)
print("Sub is ", result1)