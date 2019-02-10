# Chapter 11 Question 5
# Write a function to add two matrices.


def add_matrices(left, right):
    result = []
    for i in range(len(left)):
        innerList = []
        for j in range(len(left)):
            innerList.append(left[i][j] + right[i][j])
        result.append(innerList)
    return result


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


def main():
    size = eval(input("Enter size of both Matrices: "))
    print("Number in first matrix:", end="\t")
    left = [float(x) for x in input().split()]
    left = list_matrix(size, left)
    print("Number in second matrix:", end="\t")
    right = [float(x) for x in input().split()]
    right = list_matrix(size, right)
    print("Sum of Matrices are : ")
    print_matrix(add_matrices(left, right))


if __name__ == "__main__":
    main()
