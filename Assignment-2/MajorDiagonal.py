# Chapter 11 Question 2
# Write a function that sums all the numbers
# of the major diagonal in an M X N matrix of integers


def sumMajorDiagonal(m):
    sum = 0
    for i in range(len(m)):
        sum += m[i][i]

    return sum


def main():
    size = eval(input("Enter Size of the Matrix : "))
    matrix = [
        [float(x) for x in
         input("Enter a " + str(size) + "-by-" + str(size) + "matrix row for row " + str(i + 1) + " : ").split()] for
        i in range(size)]

    print("Sum of the elements in the major diagonal is", sumMajorDiagonal(matrix))


if __name__ == "__main__":
    main()
