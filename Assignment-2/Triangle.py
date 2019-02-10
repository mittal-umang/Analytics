# Chapter 12 Question 1
from GeometricObject import GeometricObject


class Triangle(GeometricObject):
    def __init__(self, color, isFilled, side1=1.0, side2=1.0, side3=1.0):
        super().__init__(color, isFilled)
        self.__side1 = int(side1)
        self.__side2 = int(side2)
        self.__side3 = int(side3)

    def getSide1(self):
        return self.__side1

    def getSide2(self):
        return self.__side2

    def getSide3(self):
        return self.__side3

    def getPerimeter(self):
        return self.getSide1() + self.getSide2() + self.getSide3()

    def getArea(self):
        s = self.getPerimeter() / 2
        return (s * (s - self.getSide1()) * (s - self.getSide2()) * (s - self.getSide3())) ** 0.5

    def __str__(self):
        return "Triangle: side1 = " + str(self.getSide1()) + " side2 = " + str(self.getSide2()) + " side3 = " + str(
            self.getSide3())


def main():
    side1, side2, side3, color, isFilled = input("Enter Sides of triangle,its color and 1 or 0 for filled:").split(",")
    triangle = Triangle(color, bool(isFilled), side1, side2, side3)
    print("Area of triangle", triangle.getArea())
    print("Perimeter of triangle", triangle.getPerimeter())
    print("Color of triangle", triangle.getColor())
    print("Triangle is filled", triangle.isFilled())


if __name__ == "__main__":
    main()
