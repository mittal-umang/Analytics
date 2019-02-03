# Chapter 5 Question 54
# Write a program that draws a diagram for the
# function f(x) = x2

import turtle


def drawLine(x1, y1, x2, y2):
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.goto(x2, y2)
    turtle.penup()


def main():
    drawLine(-250, 0, 250, 0)
    drawLine(0, -150, 0, 150)
    drawLine(-25, 125, 0, 150)
    drawLine(0, 150, 25, 125)
    drawLine(225, 25, 250, 0)
    drawLine(250, 0, 225, -25)
    turtle.penup()
    turtle.goto(-30, 100)
    turtle.pendown()
    i = -10
    while i < 11:
        turtle.goto(3 * i, i ** 2)
        i += 1
    turtle.done()


if __name__ == "__main__":
    main()
