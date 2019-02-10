# Chapter 8 Question 2
# Write your own function to implement
# find. Write a program that prompts the user to enter two strings and then checks
# whether the first string is a substring of the second string.


def findSubString(s, sub):
    start = 0
    end = 0
    while start < len(s):
        if s[start + end] != sub[end]:
            start += 1
            end = 0
            continue
        end += 1
        if end == len(sub):
            return True
    return False


def main():
    s = input("Enter main string : ")
    sub = input("Enter sub string : ")
    if findSubString(s, sub):
        print("String Found")
    else:
        print("String not Found")


if __name__ == "__main__":
    main()
