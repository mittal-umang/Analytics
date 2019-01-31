# Chapter 4 Question 21
# Zeller’s congruence is an algorithm developed by
# Christian Zeller to calculate the day of the week

from math import floor


def __day__(daynumber):
    week = {
        0: "Saturday",
        1: "Sunday",
        2: "Monday",
        3: "Tuesday",
        4: "Wednesday",
        5: "Thursday",
        6: "Friday"

    }
    return week.get(daynumber, "Invalid Day")


def __zeller__(year, month, day):
    if month == 1 or month == 2:
        year = year - 1
        month = month + 12
    q = day
    m = month
    j = floor(year / 100)
    k = year % 100
    h = (q + floor(26 * (m + 1) / 10) + k + floor(k / 4) + floor(j / 4) + 5 * j) % 7
    return __day__(h)


def __main__():
    year = eval(input("Enter year (e.g : 2008):"))
    month = eval(input("Enter Month (1-12):"))
    if month > 12:
        print("Entered month is invalid. Exiting...")
        return None
    day = eval(input("Enter the  of the month (1-31):"))
    if day > 31:
        print("Entered day is invalid. Exiting...")
        return None
    elif year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        if month == 2 and day > 29:
            print("Entered day cannot be evaluate since year is a leap year and the days is not in February")
            print("Exiting....")
            return None
    elif month == 2 and day > 28:
        print("Entered day cannot exist in February. Exiting...")
        return None
    print("Day of the week is", __zeller__(year, month, day))


__main__()
