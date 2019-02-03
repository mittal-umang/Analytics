# Chapter 1 Question 18
# (Turtle: draw a star) Write a program that draws a star, as shown in Figure 1.19c.
# (Hint: The inner angle of each point in the star is 36 degrees.)

import turtle


def __drawTurtle__():
    for i in range(5):
        turtle.forward(100)
        turtle.left(180)
        turtle.left(36)
    turtle.done()


if __name__ == "__main__":
    __drawTurtle__()
