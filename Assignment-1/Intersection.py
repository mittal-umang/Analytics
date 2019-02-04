# Chapter 7 Question 9
# Suppose two line segments intersect. The two endpoints
# for the first line segment are (x1, y1) and (x2, y2) and for the second line segment
# are (x3, y3) and (x4, y4). Write a program that prompts the user to enter these
# four endpoints and displays the intersecting point.

from LinerEquation import LinerEquation


def __equationConstant__(x1, y1, x2, y2):
    m = (y1 - y2) / (x2 - x1)
    c = m * x1 + y1
    return m, 1, c


def main():
    x1, y1, x2, y2 = eval(input("Enter Coordinates of first line in order : "))
    x3, y3, x4, y4 = eval(input("Enter Coordinates of second line in order : "))
    linerEquation = LinerEquation(__equationConstant__(x1, y1, x2, y2), __equationConstant__(x3, y3, x4, y4))
    print("in main")
    if not linerEquation.isSolvable():
        print("The equation has no solution")
    else:
        print("The intersecting point is: (", linerEquation.getX(), ",", linerEquation.getY(), ")")


if __name__ == "__main__":
    main()
