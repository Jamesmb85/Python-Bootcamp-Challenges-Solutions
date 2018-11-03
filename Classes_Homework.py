# Object Oriented Programming
# Homework Assignment
# Problem 1
#
# Fill in the Line class methods to accept coordinates as a pair of tuples and return the slope and distance of the line.

import math

class Line:

    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        x1, y1 = self.coor1 #coordinates are unpacked into variables
        x2, y2 = self.coor2
        return float(( ((x2-x1)**2) + ((y2-y1)**2) )**(1/2))

    def slope(self):
        x1, y1 = self.coor1 #coordinates are unpacked into variables
        x2, y2 = self.coor2
        return float(((y2 -y1)/(x2 -x1)))


coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)

print(li.distance())
print(li.slope())


# Problem 2
# Fill in the class



class Cylinder:

    #class attribute
    pi = 3.14

    def __init__(self,height,radius):
        self.height = height
        self.radius = radius

    def volume(self):
        return Cylinder.pi * self.height* self.radius**2

    def surface_area(self):
        return (2 * Cylinder.pi * self.radius * self.height) + (2 * Cylinder.pi * self.radius**2)



c = Cylinder(2,3)
print(c.volume())
print(c.surface_area())