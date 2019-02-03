# Chapter 3 Question 3
# Find the GPS locations for Atlanta, Georgia;
# Orlando, Florida; Savannah, Georgia; and Charlotte, North Carolina from
# www.gps-data-team.com/map/ and compute the estimated area enclosed by these
# four cities.


import math


def __calculateside__(x1, y1, x2, y2):
    x1 = x1 * math.pi / 180
    y1 = y1 * math.pi / 180
    x2 = x2 * math.pi / 180
    y2 = y2 * math.pi / 180
    d = 6371.01 * math.acos(math.sin(x1) * math.sin(x2) + math.cos(x1) * math.cos(x2) * math.cos(y1 - y2))
    return d


def __semiperimeter__(side1, side2, side3):
    return (side1 + side2 + side3) / 2


def __area__(x1, y1, x2, y2, x3, y3):
    side1 = __calculateside__(x1, y1, x2, y2)
    side2 = __calculateside__(x2, y2, x3, y3)
    side3 = __calculateside__(x3, y3, x1, y1)
    semi = __semiperimeter__(side1, side2, side3)

    return (semi * (semi - side1) * (semi - side2) * (semi - side3)) ** 0.5


def main():
    ATLx = 33.7242700
    ATLy = -84.5785800
    ORLx = 28.4115300
    ORLy = -81.5250400
    SAVx = 32.1672300
    SAVy = -81.1998900
    CHAx = 35.2072400
    CHAy = -80.9567600

    area1 = __area__(ATLx, ATLy, ORLx, ORLy, SAVx, SAVy)
    area2 = __area__(ATLx, ATLy, CHAx, CHAy, SAVx, SAVy)

    print("The geographical area is :", area1 + area2, "sq. km")


if __name__ == "__main__":
    main()
