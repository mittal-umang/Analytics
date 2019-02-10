# Chapter 10 Question 15
# Write the following function that returns true if the list is already
# sorted in increasing order


def isSorted(list):
    for i in range(len(list) - 1):
        if list[i] > list[i + 1]:
            return False
    return True


def main():
    print("Enter a list of numbers : ")
    numberList = [int(x) for x in input().split()]
    if isSorted(numberList):
        print("The list is already sorted")
    else:
        print("The list is not sorted")


if __name__ == "__main__":
    main()
