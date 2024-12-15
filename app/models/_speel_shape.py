import math
from enum import Enum
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_area(self, area: float, width: int = 1) -> float:
        pass
    
class Triangle(Shape):
    def calculate_area(self, area, width = 1) -> float:
        return (math.sqrt(3) / 4) * area ** 2
    
class Circle(Shape):
    def calculate_area(self, area, width = 1) -> float:
        return math.pi * (area ** 2)
    
class Square(Shape):
    def calculate_area(self, area, width = 1) -> float:
        return area ** 2
    
class Line(Shape):
    def calculate_area(self, area, width = 1) -> float:
        return area * width

class SpellShape(Enum):
    TRIANGLE = Triangle()
    CIRCLE = Circle()
    SQUARE = Square()
    LINE = Line()