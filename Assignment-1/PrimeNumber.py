# Chapter 6 Question 10
# Write a number to find all the prime numbers below a given number


def isPrime(number):
    i = 2
    while i <= number / 2:
        if number % i == 0:
            return False
        i += 1
    return True


def main():
    maxNumber = eval(input("Enter the a number upto whose prime numbers are required: "))
    count = 0
    primeNumber = 2
    while primeNumber < maxNumber:
        if isPrime(primeNumber):
            print(primeNumber, end=" ")
            count += 1
            if count % 10 == 0:
                print()

        primeNumber += 1


if __name__ == "__main__":
    main()

