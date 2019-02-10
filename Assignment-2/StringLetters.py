# Chapter 8 Question 6
# Write a function that counts the number of letters in
# a string using the following header:
# Write a test program that prompts the user to enter a string and displays the number
# of letters in the string.


import re


def countLetters(s):
    return len("".join(re.findall("[a-zA-Z]", s)))


def main():
    inputString = input("Enter string to count number of letters : ")
    print("There are ", countLetters(inputString), "letter in ", inputString)


if __name__ == "__main__":
    main()
