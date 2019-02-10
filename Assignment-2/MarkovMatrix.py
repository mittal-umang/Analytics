# Chapter 11 Question 25
# An n x n matrix is called a positive Markov matrix if each element
# is positive and the sum of the elements in each column is 1. Write the following
# function to check whether a matrix is a Markov matrix

def print_matrix(sqMatrix):
    for i in range(len(sqMatrix)):
        for j in range(len(sqMatrix)):
            print(sqMatrix[i][j], end="\t")
        print()


def list_matrix(size, alist):
    i = 0
    result = []
    while i < len(alist):
        result.append(alist[i:i + size])
        i += size
    return result


def isMarkovMatrix(matrix):
    for i in range(len(matrix)):
        sum = 0
        for j in range(len(matrix)):
            if 0 < matrix[j][i] < 1:
                sum += matrix[j][i]
            else:
                return False
        if not (sum == 1):
            return False
    return True


def main():
    size = eval(input("Enter Size of Matrix: "))
    print("Enter matrix row by row:")
    matrix = [[float(x) for x in input().split()] for i in range(size)]
    if isMarkovMatrix(matrix):
        print("It is a Markov matrix")
    else:
        print("It is not a Markov matrix")


if __name__ == "__main__":
    main()
