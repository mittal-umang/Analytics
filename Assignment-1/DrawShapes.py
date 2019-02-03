# Chapter 3 Question 16
# Write a program that draws a triangle, square, pentagon,
# hexagon, and octagon, Note that the bottom edges of
# these shapes are parallel to the x-axis.

import turtle


def __drawShape__(x, angle, edge):
    turtle.penup()
    turtle.goto(x, 0)
    turtle.pendown()
    while edge > 0:
        turtle.forward(50)
        turtle.left(angle)
        edge -= 1


def main():
    edge = 3
    distance = -300
    while edge < 9:
        angle = 180 - (edge - 2) * 180 / edge
        if edge != 7:
            __drawShape__(distance, angle, edge)
        else:
            pass
        distance += 100
        edge += 1

    turtle.done()


if __name__ == "__main__":
    main()
