import math


class Circle:

    def __init__(self, radius):
        if type(radius) not in [int, float]:
            raise TypeError("Радиус должен быть числом (целым или с плавающей точкой)")
        if radius < 0:
            raise ValueError("Радиус должен быть положительным числом")
        self.radius = radius
    
    def get_radius(self):
        return self.radius
    
    def get_diameter(self):
        return self.radius * 2
    
    def get_perimeter(self):
        return 2 * self.radius * math.pi
