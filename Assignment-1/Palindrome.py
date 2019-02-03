# Chapter 6 Question 3
# Write a program to find the palindrome of a number using two functions reverse() and isPalindrone()


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
    inputNumber = eval(input("Enter a number to check if it is palindrome: "))
    if isPalindrome(inputNumber):
        print("The number entered is a palindrome.")
    else:
        print("The number entered is NOT a palindrome")


if __name__ == "__main__":
    main()
