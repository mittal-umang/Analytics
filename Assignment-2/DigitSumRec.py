# Chapter 15 Question 1
# Write a recursive function that computes
# the sum of the digits in an integer.


def sumDigits(number):
    if number == 0:
        return 0
    else:
        return sumDigits(number // 10) + number % 10


def main():
    inputNumber = eval(input("Enter Number: "))
    print("Sum of digits is", sumDigits(inputNumber))


if __name__ == "__main__":
    main()
