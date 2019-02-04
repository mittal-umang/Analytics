# Chapter 6 Question 41
# Use the functions defined in Listing
# 6.14 to write a program that displays a rectangle centered at with width
# and height 100 and a circle centered at (50, 0) with radius 50. Fill 10 random
# points inside the rectangle and 10 inside the circle,
import turtle
import random


def __drawRectangle__(x, y, height, width):
    turtle.penup()
    turtle.goto(int(x + (height / 2)), y)
    turtle.left(90)
    turtle.pendown()
    turtle.forward(height / 2)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height / 2)


def randomPointRect():
    x = random.randint(-124, -24)
    y = random.randint(-49, 49)
    return x, y


def randomPointCircle():
    x = random.randint(0, 99)
    y = random.randint(-49, 49)
    return x, y


def main():
    __drawRectangle__(-75, 0, 100, 100)
    turtle.penup()
    turtle.goto(100, 0)
    turtle.pendown()
    turtle.circle(50)
    i = 0
    turtle.penup()
    while i < 11:
        turtle.goto(randomPointRect())
        turtle.dot()
        i += 1

    i = 0
    while i < 11:
        turtle.penup()
        x, y = randomPointCircle()
        if (x - 50) ** 2 + y ** 2 < 2500:
            turtle.goto(randomPointCircle())
            turtle.dot()
            i += 1
        else:
            pass

    turtle.done()


if __name__ == "__main__":
    main()
