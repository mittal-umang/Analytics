# Chapter 5 Question 53
# Write a program that plots the sine
# function in red and cosine in blue

import turtle
import math


def drawLine(x1, y1, x2, y2):
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.goto(x2, y2)
    turtle.penup()


def main():
    drawLine(-360, 0, 360, 0)
    drawLine(0, -150, 0, 150)
    drawLine(-20, 125, 0, 150)
    drawLine(0, 150, 20, 125)
    drawLine(340, -25, 360, 0)
    drawLine(360, 0, 340, 25)

    turtle1 = turtle.Turtle()
    turtle2 = turtle.Turtle()
    turtle1.penup()
    turtle2.penup()
    turtle1.goto(-360, 50 * math.sin(math.radians(-360)))
    turtle2.goto(-360, 50 * math.cos(math.radians(-360)))
    turtle1.pendown()
    turtle2.pendown()
    turtle1.pencolor("red")
    turtle2.pencolor("blue")
    i = -360
    while i < 361:
        turtle1.goto(i, 50 * math.sin(math.radians(i)))
        turtle2.goto(i, 50 * math.cos(math.radians(i)))
        i += 1
    turtle.done()


if __name__ == "__main__":
    main()
