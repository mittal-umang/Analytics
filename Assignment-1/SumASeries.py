# Chapter 5 Question 26
# Sum a series


def main():
    lastNumber = eval(input("Enter the last number of the series"))
    if lastNumber % 2 == 0:
        lastNumber -= 1

    sum = 0
    while lastNumber > 1:
        sum += (lastNumber - 2) / lastNumber
        lastNumber -= 2

    print("Sum of the series is", sum)


if __name__ == "__main__":
    main()
