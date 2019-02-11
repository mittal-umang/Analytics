def locate_largest(mat):
    max_loc = [0, 0]
    max_item = mat[0][0]
    for row in range(len(mat)):
        for col in range(len(mat[0])):
            if mat[row][col] > max_item:
                max_loc = [row, col]
                max_item = mat[row][col]
    return tuple(max_loc)


def main():
    size = eval(input("Enter the number of rows:"))
    inputMatrix = [[float(x) for x in input("Enter a Row: ").split()] for i in range(size)]
    print("The location of the largest element is ", locate_largest(inputMatrix))


if __name__ == "__main__":
    main()
