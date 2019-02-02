# Chapter 4 Question 29
# Write a program that prompts the user to enter the center
# coordinates and radii of two circles and determines whether the second circle is
# inside the first or overlaps with the first,


def __distance__(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


def __circle_status__(dist, r1, r2):
    if dist > r1 + r2:
        return "Smaller circle lies outside Larger Circle"
    elif (r1 + r2) == dist:
        return "Circles touch Externally"
    elif abs(r1 - r2) == dist:
        return "Circle touch Internally"
    elif abs(r1 - r2) > dist:
        return "Smaller Circle lies inside Larger Circle"
    elif r1 + r2 > dist and abs(r1 - r2) > dist:
        return "Circles Overlap"


def main():
    x1, y1, r1 = eval(input("Enter circle1's center x,y coordinates and radius:"))
    x2, y2, r2 = eval(input("Enter circle2's center x,y coordinates and radius:"))
    dist = __distance__(x1, y1, x2, y2)
    print(__circle_status__(dist, r1, r2))


main()
