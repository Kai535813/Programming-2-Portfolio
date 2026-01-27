import math
class Cylinder:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height 

    def volume(self):
        radius = self.radius
        height = self.height 
        return (radius * radius) * math.pi * height 
    
    def surfaceArea(self):
        r = self.radius
        h = self.height
        return (2 * math.pi * r * h) + (2 * math.pi * (r * r))