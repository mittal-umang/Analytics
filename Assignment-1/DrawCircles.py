# Chapter 4 Question 39
# Write a program that prompts the user to enter the center
# coordinates and radii of two circles and determines whether the second circle is
# inside the first or overlaps with the first,


import turtle


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


def __draw_circle__(x, y, r):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.circle(r)


def main():
    x1, y1, r1 = eval(input("Enter circle1's center x,y coordinates and radius:"))
    x2, y2, r2 = eval(input("Enter circle2's center x,y coordinates and radius:"))
    __draw_circle__(x1, y1, r1)
    __draw_circle__(x2, y2, r2)
    dist = __distance__(x1, y1, x2, y2)
    turtle.penup()
    turtle.goto(50, 50)
    turtle.pendown()
    turtle.write(__circle_status__(dist, r1, r2), move=False, align="left")
    turtle.done()


main()
