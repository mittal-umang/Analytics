# Chapter 15 Question 21
# Write a recursive function that parses a binary number as a
# string into a decimal integer.


def binaryToDecimal(binaryString):
    if not binaryString:
        return 0
    return binaryToDecimal(binaryString[:-1]) * 2 + int(binaryString[-1])


def main():
    bString = input("Enter Binary String:")
    print("Decimal value is ", int(binaryToDecimal(bString)))


if __name__ == "__main__":
    main()
