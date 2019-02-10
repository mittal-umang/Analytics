# Chapter 10 Question 9
# Write a test program that prompts the user to enter a list of numbers and displays
# the mean and standard deviation


def mean(alist):
    sum = 0
    for i in range(len(alist)):
        sum += alist[i]
    return sum / len(alist)


def deviation(alist, mean):
    numerator = 0
    for i in range(len(alist)):
        numerator += (alist[i] - mean) ** 2

    return (numerator / (len(alist) - 1)) ** 0.5


def main():
    print("Enter a list of numbers : ")
    numberList = [float(x) for x in input().split(" ")]
    meanNumber = mean(numberList)
    print("The mean is", "%0.2f" % meanNumber)
    print("The standard deviation is", "%0.5f" % deviation(numberList, meanNumber))


if __name__ == "__main__":
    main()
