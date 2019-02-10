# Chapter 8 Question 17

class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def distance(self, point):
        return ((self.getX() - point.getX()) ** 2 + (self.getY() - point.getY()) ** 2) ** 0.5

    def isNear(self, Point):
        if self.distance(Point) < 5:
            return True
        else:
            return False

    def __str__(self):
        return "(" + str(self.getX()) + "," + str(self.getY()) + ")"


def main():
    x1, y1, x2, y2 = eval(input("Enter Coordinates of 2 point: "))
    p1, p2 = Point(x1, y1), Point(x2, y2)

    if p1.isNear(p2):
        print("Points", p1, "and", p2, "are near each other")
    else:
        print("Points", p1, "and", p2, "are NOT near each other")

    print("Distance between points is ", p1, "and", p2, "is", '%0.2f' % p1.distance(p2), "units")


if __name__ == "__main__":
    main()
