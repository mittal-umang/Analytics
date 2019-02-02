# Chapter 6 Question 24
# Write a program that displays the first 100 palindromic prime numbers. Display
# 10 numbers per line and align the numbers properly

import time


def isPrime(number):
    i = 2
    while i <= number / 2:
        if number % i == 0:
            return False
        i += 1
    return True


def reverse(number):
    reverseNumber = ""
    while number > 0:
        reverseNumber += str(number % 10)
        number = number // 10
    return int(reverseNumber)


def isPalindrome(number):
    if reverse(number) == number:
        return True
    else:
        return False


def main():
    maxNumber = eval(input("Enter the a number of palindromic prime numbers are required: "))
    count = 0
    primeNumber = 2
    while count < maxNumber:
        # Evaluating isPalindrome first to reduce the computational time of prime number.
        # since number of iterations in isPrime Functions are more.
        if isPalindrome(primeNumber) and isPrime(primeNumber):
            print(format(primeNumber, '6d'), end=" ")
            count += 1
            if count % 10 == 0:
                print()
        primeNumber += 1


if __name__ == "__main__":
    main()

