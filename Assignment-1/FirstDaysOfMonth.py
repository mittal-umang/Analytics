# Chapter 5 Question 30
# Write a program that prompts the user
# to enter the year and first day of the year, and displays the first day of each month
# in the year on the console.


def __day__(daynumber):
    week = {
        0: "Sunday",
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday"

    }
    return week.get(daynumber, "Invalid Day")


def __month__(number):
    year = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }

    return year.get(number, "Invalid Month")


def main():
    year = eval(input("Enter Year"))
    oneJanuary = eval(input("Enter first day of the year :"))
    while oneJanuary > 6:
        print("Invalid Day entered.")
        oneJanuary = eval(input("Enter first day of the year :"))
    thirtyOne = [1, 3, 5, 7, 8, 10, 12]
    thirty = [4, 6, 9, 11]
    month = 1
    print(__month__(month), ", 1 ", year, " is ", __day__(oneJanuary), sep="")
    while month < 13:
        if month in thirtyOne:
            oneJanuary += 31
        elif month in thirty:
            oneJanuary += 30
        elif month == 2:
            if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
                oneJanuary += 29
            else:
                oneJanuary += 28
        else:
            pass
        print(__month__(month), " , 1 ", year, " is ", __day__(oneJanuary), sep="")
        month += 1


if __name__ == "__main__":
    main()
