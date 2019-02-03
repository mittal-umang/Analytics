# Chapter 3 Question 19
# Write a program that prompts the user to enter two points
# and draw a line to connect the points and displays the coordinates of the points,

import turtle


def __write__(x1, y1):
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pendown()
    points = "(" + str(x1) + "," + str(y1) + ")"
    turtle.write(points, move=False, align="left")


def main():
    x1, y1, x2, y2 = eval(input("Enter the coordinates of line in order:"))
    __write__(x1, y1)
    __write__(x2, y2)
    turtle.goto(x1, y1)
    turtle.done()


if __name__ == "__main__":
    main()
