import math

class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

def display_area(shape):
    """Calculate and display the area of the given shape."""
    print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")

if __name__ == "__main__":

    shapes = [
        Circle(5),
        Rectangle(4, 6),
        Circle(3),
        Rectangle(2, 8)
    ]
    for shape in shapes:
        display_area(shape)