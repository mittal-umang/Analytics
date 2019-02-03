# Chapter 6 Question 18
# Each element is 0 or 1, which is generated randomly. Write a test program that
# prompts the user to enter n and displays an n-by-n matrix.

import random


def printMatrix(number):
    for i in range(0, number):
        for j in range(0, number):
            print(random.randint(0, 1), end=" ")
        print()


def main():
    matrixSize = eval(input("Enter the dimension of the matrix: "))
    printMatrix(matrixSize)


if __name__ == "__main__":
    main()
