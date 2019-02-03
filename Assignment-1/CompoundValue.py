# Chapter 2 Question 21
# Write a program that prompts the user to enter a monthly saving amount and
# displays the account value after the sixth month.


def __compoundValue__(value):
    return value * 1.00417


def main():
    initialAmount = eval(input("Enter the monthly saving amount "))
    month = 0
    amount = 0
    while month < 6:
        amount = __compoundValue__(initialAmount + amount)
        month += 1
    print("After the sixth month, the account value is", format(amount, '0.3f'))


if __name__ == "__main__":
    main()
