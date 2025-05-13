from abc import ABC, abstractmethod

class Shape(ABC):  # Abstract base class
    @abstractmethod
    def area(self):
        pass  # No implementation in abstract method

class Rectangle(Shape):  # Concrete subclass
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):  # Must implement the abstract method
        return self.width * self.height

# Demonstration
try:
    shape = Shape()  # This will raise an error
except TypeError as e:
    print(f"Can't instantiate abstract class: {e}")

rect = Rectangle(5, 3)
print(f"Rectangle area: {rect.area()}")  # Output: Rectangle area: 15