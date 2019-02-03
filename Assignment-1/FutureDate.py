# Chapter 4 Question 5
# Write a program that prompts the user to enter an integer for
# today’s day of the week (Sunday is 0, Monday is 1, ..., and Saturday is 6). Also
# prompt the user to enter the number of days after today for a future day and display
# the future day of the week.


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


def main():
    today = eval(input("Enter today's day:"))
    numberOfDays = eval(input("Enter the number of days elapsed since today:"))
    print("Today is", __day__(today), "and the future day is ", __day__((today + numberOfDays) % 7))


if __name__ == "__main__":
    main()

