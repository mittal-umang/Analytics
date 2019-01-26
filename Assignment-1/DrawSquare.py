# Chapter 2 Question 25
# Write a program that prompts the user to enter the
# center of a rectangle, width, and height, and displays the rectangle.


import turtle


def __draw__(x, y, height, width):
    turtle.penup()
    turtle.goto(x + (height / 2), y)
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
    turtle.done()


def __main__():
    x, y, width, height = eval(input("enter the center of a rectangle, width, and height : "))
    __draw__(x, y, height, width)


__main__()
