# Chapter 10 Question 2
# Write a program that reads a list of integers and
# displays them in the reverse order in which they were read.


def reverseList(list):
    i = len(list) - 1
    newList = []
    while i > -1:
        newList.append(int(list[i]))
        i -= 1
    return newList


def main():
    inputList = list(input("Enter numbers: "))
    print("The reversed numbers are:")
    print(str(reverseList(inputList)))


if __name__ == "__main__":
    main()
