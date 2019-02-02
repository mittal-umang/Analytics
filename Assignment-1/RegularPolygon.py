import math


class RegularPolygon:
    def __init__(self, n=3, sides=1, x=0, y=0):
        self.__numberOfSide = n
        self.__length = sides
        self.__x = x
        self.__y = y

    def getNumberOfSides(self):
        return self.__numberOfSide

    def getLength(self):
        return self.__length

    def getXCoordinate(self):
        return self.__x

    def getYCoordinate(self):
        return self.__y

    def getPerimeter(self):
        return self.getNumberOfSides() * self.getLength()

    def getArea(self):
        return (self.getNumberOfSides() * (self.getLength() ** 2)) / (4 * math.tan(math.pi / self.getNumberOfSides()))


def main():
    triangle = RegularPolygon()
    hexagon = RegularPolygon(6, 4)
    decagon = RegularPolygon(10, 4, 5.6, 7.8)

    print("The Perimeter of the triangle is ", triangle.getPerimeter(), "and area of the triangle is",
          triangle.getArea())
    print("The Perimeter of the hexagon is ", hexagon.getPerimeter(), "and area of the hexagon is",
          hexagon.getArea())
    print("The Perimeter of the decagon is ", decagon.getPerimeter(), "and area of the decagon is",
          decagon.getArea())


if __name__ == "__main__":
    main()

