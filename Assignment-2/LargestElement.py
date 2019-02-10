# Chapter 11 Question 13
# Write the following function that returns the location
# of the largest element in a two-dimensional list
import random


def locateLargest(matrix):
    return False


def main():
    size = eval(input("Enter the number of rows in the list: "))
    matrix = [
        [float(x) for x in
         input("Enter a row " + str(i + 1) + " : ").split()] for
        i in range(size)]
    list1 = [1, 2, 3, 4, 6, 6]
    print(list1.index(max(list1)))


if __name__ == "__main__":
    main()
