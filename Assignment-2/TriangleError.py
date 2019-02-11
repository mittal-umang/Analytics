# Chapter 13 Question 12
# Define an exception class named TriangleError
# that extends RuntimeError. The TriangleError class contains the private
# data fields side1, side2, and side3 with accessor methods for the three
# sides of a triangle. Modify the Triangle class in Exercise 12.1 to throw a
# TriangleError exception if the three given sides cannot form a triangle.


class TriangleError(RuntimeError):
    def __init__(self, side1, side2, side3):
        super().__init__()
        self.__side1 = side1
        self.__side2 = side2
        self.__side3 = side3

    def getSide1(self):
        return self.__side1

    def getSide2(self):
        return self.__side2

    def getSide3(self):
        return self.__side3


