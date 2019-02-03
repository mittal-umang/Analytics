# Chapter 4 Question 15
# Revise Listing 4.10, Lottery.py, to generate a three-digit lottery
# number. The program prompts the user to enter a three-digit number and determines
# whether the user wins according to the following rules:
# 1. If the user input matches the lottery number in the exact order, the award is
# $10,000.
# 2. If all the digits in the user input match all the digits in the lottery number, the
# award is $3,000.
# 3. If one digit in the user input matches a digit in the lottery number, the award is
# $1,000.


import random


def __split__(number):
    i = 0
    split = []
    while number > 0:
        split.append(number % 10)
        number = number // 10
        i += 1
    return split[2], split[1], split[0]


def __evaluate__(number):
    randomNumber = random.randint(100, 999)
    xr, yr, zr = __split__(randomNumber)
    x, y, z = __split__(number)
    if number == randomNumber:
        return 10000
    elif (x == xr and y == yr and z == zr) or (x == xr and z == yr and y == zr) or (
            x == zr and y == yr and z == xr) or (z == zr and x == yr and y == xr):
        return 3000
    elif x == xr or y == yr or z == zr or z == yr or y == zr or x == zr or z == xr or x == yr or y == xr:
        return 1000
    else:
        return 0


def main():
    userNumber = eval(input("Enter your 3 digit number:"))
    print("You have won $", __evaluate__(userNumber))


if __name__ == "__main__":
    main()
