# Complete the find_palindromes function below.

import math


def find_palindromes(year):
    cent = math.ceil(year / 100)
    startingYear = (cent - 1) * 100
    endingYear = cent * 100
    date = []
    leapYears = []
    for i in range(startingYear, endingYear):
        year = str(i)
        date.append(year[::-1] + year)
        date.append(year[:0:-1] + year)
        if (int(year) % 4 == 0 and int(year) % 100 != 0) or int(year) % 400 == 0:
            leapYears.append(int(year))

    countPalindrome = 0
    oddMonths = [1, 3, 5, 7, 8, 10, 12]
    evenMonths = [4, 6, 9, 11]

    for i in range(len(date)):
        tempString = date[i]
        if len(tempString) == 8:
            if (int(tempString[0] + tempString[1]) in oddMonths and int(tempString[2] + tempString[3]) < 32) or (
                    int(tempString[0] + tempString[1]) in evenMonths and int(tempString[2] + tempString[3]) < 31) \
                    or (int(tempString[-4:]) in leapYears and int(tempString[2] + tempString[3]) < 30 and int(
                tempString[0] + tempString[1]) == 2) \
                    or (int(tempString[-4:]) not in leapYears and int(tempString[2] + tempString[3]) < 29 and int(
                tempString[0] + tempString[1]) == 2):
                countPalindrome += 1
        elif len(tempString) == 7:
            if (int(tempString[0]) in oddMonths and int(tempString[1] + tempString[2]) < 32) or (
                    int(tempString[0]) in evenMonths and int(tempString[1] + tempString[2]) < 31) \
                    or (int(tempString[-4:]) in leapYears and int(tempString[1] + tempString[2]) < 30 and int(
                tempString[0]) == 2) \
                    or (int(tempString[-4:]) not in leapYears and int(tempString[1] + tempString[2]) < 29 and int(
                tempString[0]) == 2):
                countPalindrome += 1

    return countPalindrome


if __name__ == '__main__':
    print(find_palindromes(2019))
