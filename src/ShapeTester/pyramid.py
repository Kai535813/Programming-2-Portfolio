import math
class Pyramid:
    def __init__(self, height, length, width):
        self.height = height
        self.length = length
        self.width = width 

    def volume(self):
        h = self.height
        l = self.length
        w = self.width 
        return l * w * h * 1/3
    def surfaceArea(self):
        h = self.height
        l = self.length
        w = self.width 
        return (l*w)+(l* math.sqrt((w/2)**2 + h**2)) + (w * math.sqrt((l/2)**2 + h**2))

        