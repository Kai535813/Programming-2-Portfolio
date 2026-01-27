import math 
class Sphere:
    def __init__(self, radius):
        self.radius = radius
    def volume(self):
        return 4/3 * math.pi * self.radius**3 
    def surfaceArea(self):
        return 4 * math.pi * self.radius**2
        