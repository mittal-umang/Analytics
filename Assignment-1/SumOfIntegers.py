# Chapter 2 Question 6
# Write a program that reads an integer between 0 and
# 1000 and adds all the digits in the integer. For example, if an integer is 932, the
# sum of all its digits is 14.

# ## this code can work for any number of digits. limiting the values through user input as asked in question.


def main():
    number = eval(input("Enter a number between 0 and 1000 : "))
    print("The sum of digits is", _sum_(number))


def _sum_(number):
    sumofDigits = 0
    while number > 0:
        sumofDigits += number % 10
        number = number // 10
    return sumofDigits


if __name__ == "__main__":
    main()
