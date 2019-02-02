# Chapter 6 Question 29
# Write a program that prompts the user to enter a credit card number as an integer


def getDigit(number):
    sum = 0
    while number > 0:
        sum += number % 10
        number = number // 10
    return sum


def sumOfDoubleEvenPlace(number):
    count = 1
    sumOfDoubleEvenPlace = 0
    while number > 0:
        digit = number % 10
        number = number // 10
        if count % 2 == 0:
            if digit > 4:
                sumOfDoubleEvenPlace += getDigit(2 * digit)
            else:
                sumOfDoubleEvenPlace += 2 * digit
        else:
            pass
        count += 1

    return sumOfDoubleEvenPlace


def sumOfOddPlace(number):
    count = 1
    sumOfOddPlace = 0
    while number > 0:
        digit = number % 10
        number = number // 10
        if count % 2 != 0:
            sumOfOddPlace += digit
        else:
            pass
        count += 1
    return sumOfOddPlace


def getSize(number):
    size = 0
    while number > 0:
        size += 1
        number = number // 10
    return size


def getPrefix(number, k):
    if getSize(number) < k:
        return number
    else:
        return number // 10 ** (getSize(number) - k)


def prefixMatched(number):
    if getPrefix(number, 1) == 4 or getPrefix(number, 1) == 5 or getPrefix(number, 1) == 6 or getPrefix(number,
                                                                                                        2) == 37:
        return True
    else:
        return False


def isValid(number):
    if 13 < getSize(number) < 17 and prefixMatched(number):
        if (sumOfOddPlace(number) + sumOfDoubleEvenPlace(number)) % 10 == 0:
            return "Card is Valid"
        else:
            return "Card is Invalid"
    else:
        return "Card is Invalid"


def main():
    cardNumber = eval(input("Enter Credit Card Number : "))
    print(isValid(cardNumber))


if __name__ == "__main__":
    main()
