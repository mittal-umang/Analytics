# Chapter 4 Question 24
# Write a program that simulates picking a card from a deck of
# 52 cards. Your program should display the rank (Ace, 2, 3, 4, 5, 6, 7, 8, 9, 10,
# Jack, Queen, King) and suit (Clubs, Diamonds, Hearts, Spades) of the card.

import random


def __suite__(suiteNumber):
    suites = {
        0: "Clubs",
        1: "Diamonds",
        2: "Hearts",
        3: "Spades"
    }
    return suites.get(suiteNumber, "Invalid Suite")


def main():
    cardNumber = random.randint(1, 13)
    suiteNumber = random.randint(1, 3)
    if cardNumber == 1:
        cardNumber = "Ace"
    elif cardNumber == 11:
        cardNumber = "Jack"
    elif cardNumber == 12:
        cardNumber = "Queen"
    elif cardNumber == 13:
        cardNumber = "King"
    else:
        pass
    print("The card you picked is the ", cardNumber, " of ", __suite__(suiteNumber))


if __name__ == "__main__":
    main()
