# Chapter 11 Question 6
# Write a function to multiply two matrices


def multiply_matrix(left, right):
    result = []
    for i in range(len(left)):
        innerMatrix = []
        for j in range(len(left)):
            sum = 0
            for k in range(len(left)):
                sum += left[i][k] * right[k][j]
            innerMatrix.append(sum)
        result.append(innerMatrix)
    return result


def print_matrix(sqMatrix):
    for i in range(len(sqMatrix)):
        for j in range(len(sqMatrix)):
            print('%0.2f' % sqMatrix[i][j], end="\t", sep="\t")
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
    print("Enter Matrix 1:", end="\t")
    left = [float(x) for x in input().split()]
    left = list_matrix(size, left)
    print("Enter Matrix 2:", end="\t")
    right = [float(x) for x in input().split()]
    right = list_matrix(size, right)
    print("Product of Matrices are : ")
    print_matrix(multiply_matrix(left, right))


if __name__ == "__main__":
    main()
