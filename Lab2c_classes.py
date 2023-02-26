#Jonathan Chornay
#CMSY 257 Spring 2023 Class
#Professor Charles Edwards
#
#Lab 2 Problem 3 classes
import math

class GeometricObject:

    def __init__(self, color, filled):
        self.__color = str(color)
        self.__filled = bool(filled)

    #getters and setters
    def get_color(self):
        return self.__color
    def set_color(self, color):
        self.__color = color

    def get_filled(self):
        return self.__filled
    def set_filled(self, filled):
        self.__filled = filled

class Triangle(GeometricObject):

    # default constructor for triangle with sides of length 1.0
    def __init__(self):
        super().__init__("blue", True)
        self.__side1 = 1.0
        self.__side2 = 1.0
        self.__side3 = 1.0

    #getters and setters
    def get_side1(self):
        return self.__side1
    def set_side1(self, side1):
        self.__side1 = side1

    def get_side2(self):
        return self.__side2
    def set_side2(self, side2):
        self.__side2 = side2

    def get_side3(self):
        return self.__side3
    def set_side3(self, side3):
        self.__side3 = side3

    #method to calculate area using Heron's Formula from https://www.cuemath.com/measurement/area-of-triangle-with-3-sides/
    def getArea(self):
        a = self.__side1
        b = self.__side2
        c = self.__side3
        s = (a+b+c)/2
        A = math.sqrt(s*(s-a)*(s-b)*(s-c))

        return A

    #method to calculate perimeter
    def getPerimeter(self):
        return self.__side1 + self.__side2 + self.__side3

    #__str__ method for triangle
    def __str__(self):
        return f"Triangle: " \
               f"\n\tside 1 = {self.__side1:.1f}" \
               f"\n\tside 2 = {self.__side2:.1f}" \
               f"\n\tside 3 = {self.__side3:.1f}"