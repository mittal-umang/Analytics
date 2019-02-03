# Chapter 5 Question 55
# Write a program to draw a chessboard
import turtle


def drawBox(startX, startY, size, color):
    turtle.penup()
    turtle.goto(startX, startY)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()

    for i in range(0, 4):
        turtle.forward(size)
        turtle.right(90)
    turtle.end_fill()


def main():
    color = "black"
    startX = -150
    startY = -150
    boxSize = 50
    turtle.penspeed(10)
    for i in range(0, 8):
        for j in range(0, 8):
            drawBox(startX + j * boxSize, startY + i * boxSize, boxSize, color)
            color = 'black' if color == 'white' else 'white'
        color = 'black' if color == 'white' else 'white'

    turtle.done()


if __name__ == "__main__":
    main()
