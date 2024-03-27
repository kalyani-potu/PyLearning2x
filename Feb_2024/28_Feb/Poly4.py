class Shape:
    def area(self):
        print('Area of the shape')
class Rectangle(Shape):
    def __init__(self, length,width):
        self.l = length
        self.w = width
    def area(self):
        return self.l*self.w

class Circle(Shape):
    def __init__(self, radius):
        self.r = radius
    def area(self):
        return 3.14*self.r**2

shape1 = Rectangle(3,4)
print(shape1.area())
shape2 = Circle(10)
print(shape2.area())
shape3 = Shape()
shape3.area()


