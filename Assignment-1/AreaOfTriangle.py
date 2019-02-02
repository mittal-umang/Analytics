# Chapter 2 Question 14
# Write a program that prompts the user to enter the
# three points (x1, y1), (x2, y2), and (x3, y3) of a triangle and displays its area.
# use Heron's formula


def __calculateside__(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


def __semiperimeter__(side1, side2, side3):
    return (side1 + side2 + side3) / 2


def __area__(side1, side2, side3):
    semi = __semiperimeter__(side1, side2, side3)
    return (semi * (semi - side1) * (semi - side2) * (semi - side3)) ** 0.5


def main():
    x1, y1, x2, y2, x3, y3 = eval(input("Enter the coordiantes of the triangle (continously) : "))

    side1 = __calculateside__(x1, y1, x2, y2)
    side2 = __calculateside__(x2, y2, x3, y3)
    side3 = __calculateside__(x1, y1, x3, y3)
    area = __area__(side1, side2, side3)
    print("The area of the triangle is", '%.1f' % area,"sq. units")


main()
