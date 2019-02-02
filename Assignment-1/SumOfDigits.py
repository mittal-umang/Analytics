# Chapter 6 Question 2
# Write a function that computes the sum of the digits
# in an integer.


def sumDigits(number):
    sumOfDigits = 0
    while number > 0:
        sumOfDigits += number % 10
        number = number // 10
    return sumOfDigits


def main():
    inputNumber = eval(input("Enter integer: "))
    print("The sum of the digits of ", inputNumber, "is", sumDigits(inputNumber))


if __name__ == "__main__":
    main()
