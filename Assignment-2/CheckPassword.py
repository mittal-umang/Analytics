# Chapter 8 Question 3
# Write a function that checks whether a string is a valid password. Suppose the password
# rules are as follows:
# ■ A password must have at least eight characters.
# ■ A password must consist of only letters and digits.
# ■ A password must contain at least two digits.

import re


def checkString(string):
    findString = "".join(re.findall("[~!@#$%^&*(){}:;'?/>.<,]", string))
    if len(findString) > 0:
        return False
    else:
        return True


def numberOfDigits(string):
    return len("".join(re.findall("\d+", string)))


def isPasswordValid(string):
    if len(string) >= 8 and checkString(string) and numberOfDigits(string) > 2:
        return True
    else:
        return False


def main():
    inputPassword = input("Enter Password : ")
    if isPasswordValid(inputPassword):
        print("Password is valid")
    else:
        print("Password NOT Valid")


if __name__ == "__main__":
    main()
