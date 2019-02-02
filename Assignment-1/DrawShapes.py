# Chapter 3 Question 16
# Write a program that draws a triangle, square, pentagon,
# hexagon, and octagon, Note that the bottom edges of
# these shapes are parallel to the x-axis.

import turtle


def __draw__(radius, edges, distance):
    turtle.penup()
    turtle.goto(distance, 0)
    turtle.pendown()
    i = 0
    print(((edges - 2) * 180) / edges)
    while i < edges:
        turtle.forward(radius)
        turtle.left(((edges - 2) * 180) / edges)
        i += 1


def main():
    i = 3
    distance = 0
    while i < 9:
        if i != 7:
            print(i)
            __draw__(30, i, distance)
            distance += 70
        i += 1
    turtle.done()

main()
