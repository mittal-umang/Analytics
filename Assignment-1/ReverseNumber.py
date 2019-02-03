# Chapter 3 Question 11
# Write a program that prompts the user to enter a four-digit integer
# and displays the number in reverse order.


def __reverse__(number):
    reverseNumber = ""
    while number > 0:
        reverseNumber += str(number % 10)
        number = number // 10
    return reverseNumber


def main():
    number = eval(input("Enter an integer: "))
    reversedNumber = __reverse__(number)
    print("The reversed number is", reversedNumber)


if __name__ == "__main__":
    main()

