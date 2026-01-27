from box import Box 
from sphere import Sphere 
from pyramid import Pyramid 
from cylinder import Cylinder 


print("Find the volume and surface area of a chosen shape.")
shape = input("Please type, Box, Sphere, Pyramid or Cylinder to continue: ")

if shape == "Box":
    length = input("Enter length: ")
    width = input("Enter width: ")
    height = input("Enter height: ")
    def main():
        box = Box(height,width,length)
        print("Box Volume: ", box.volume())
        print("Box Surface Area: ", box.surface_area())

elif shape == "Sphere":
    radius = float(input("Enter radius: "))
    sphere = Sphere(radius)
    print("Sphere Volume: ",sphere.volume())
    print("Sphere Surface Area: ",sphere.surfaceArea())
    

elif shape == "Pyramid":
    height = float(input("Enter height: "))
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    pyramid = Pyramid(height, length, width)
    print("Pyramid Volume: ", pyramid.volume())
    print("Pyramid Surface Area: ", pyramid.surfaceArea())

elif shape == "Cylinder":
    height = float(input("Enter height: "))
    radius = float(input("Enter Radius: "))
    cylinder = Cylinder(height, radius)
    print("Cylinder Volume: ", cylinder.volume())
    print("Cylinder Surface Area: ", cylinder.surfaceArea())



    


        