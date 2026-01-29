from box import Box 
from sphere import Sphere 
from pyramid import Pyramid 
from cylinder import Cylinder 


print("Find the volume and surface area of a chosen shape.")
again = input("Would you like to start? If so type yes: ")
while again == "yes":
    shape = input("Please type, Box, Sphere, Pyramid or Cylinder to continue: ")
    if shape == "Box":
        length = float(input("Enter length: "))
        width = float(input("Enter width: "))
        height = float(input("Enter height: "))
        box = Box(length,width,height)
        print("Box Volume: ", box.volume())
        print("Box Surface Area: ", box.surface_area())
        again = input("Want to go again? If so type yes: ")

    elif shape == "Sphere":
        radius = float(input("Enter radius: "))
        sphere = Sphere(radius)
        print("Sphere Volume: ",sphere.volume())
        print("Sphere Surface Area: ",sphere.surfaceArea())
        again = input("Want to go again? If so type yes: ")


    elif shape == "Pyramid":
        height = float(input("Enter height: "))
        length = float(input("Enter length: "))
        width = float(input("Enter width: "))
        pyramid = Pyramid(height, length, width)
        print("Pyramid Volume: ", pyramid.volume())
        print("Pyramid Surface Area: ", pyramid.surfaceArea())
        again = input("Want to go again? If so type yes: ")

    elif shape == "Cylinder":
        height = float(input("Enter height: "))
        radius = float(input("Enter Radius: "))
        cylinder = Cylinder(height, radius)
        print("Cylinder Volume: ", cylinder.volume())
        print("Cylinder Surface Area: ", cylinder.surfaceArea())
        again = input("Want to go again? If so type yes: ")
print("Bye bye!")



    


        