# Chapter 11 Question 10
# Write a program that randomly fills in 0s and 1s into
# a 4 X 4 matrix, prints the matrix, and finds the rows and columns with the most
# 1s.


import random


def random_matrix(size):
    result = []
    for i in range(size):
        innerList = []
        for j in range(size):  # inner for loop
            innerList.append(random.randint(0, 1))
        result.append(innerList)

    return result


def print_matrix(sqMatrix):
    for i in range(len(sqMatrix)):
        for j in range(len(sqMatrix)):
            print(sqMatrix[i][j], end="\t")
        print()


def col_sum(matrix):
    sumList = []
    for i in range(len(matrix)):
        sum = 0
        for j in range(len(matrix)):
            sum += matrix[j][i]
        sumList.append(sum)
    return sumList


def row_sum(matrix):
    sumList = []
    for i in range(len(matrix)):
        sum = 0
        for j in range(len(matrix)):
            sum += matrix[i][j]
        sumList.append(sum)
    return sumList


def largest_index(sumList):
    largestNumber = max(sumList)
    largestIndex = []
    for i in range(len(sumList)):
        if sumList[i] == largestNumber:
            largestIndex.append(i)
    return largestIndex


def main():
    size = eval(input("Enter Size of Matrix: "))
    matrix = random_matrix(size)
    print_matrix(matrix)
    print("The largest row index : ", largest_index(row_sum(matrix)))
    print("The largest Column index : ", largest_index(col_sum(matrix)))


if __name__ == "__main__":
    main()
