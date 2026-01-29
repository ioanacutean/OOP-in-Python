import math

class Shape:
    def __init__(self, ):
        pass

    def area(self):
        pass

    def __str__(self):
        return f"Generic shape"

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        super().area()
        return "{:.2f}".format(math.pi * self.radius ** 2)

    def __str__(self):
        return f"Circle with radius {self.radius}."

class Rectangle(Shape):
    def __init__(self, width, height):
        super().area()
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __str__(self):
        return f"Rectangle with width {self.width} and length {self.height}"


circle = Circle(5.0)
rectangle = Rectangle(4.0, 6.0)
print(circle.area()) # outputs: 78.54 (assuming π = 3.1416)
print(rectangle.area()) # outputs: 24.0
print(circle) # outputs: "Circle with radius 5.0"
print(rectangle) # outputs: "Rectangle with length 4.0 and width 6.0"