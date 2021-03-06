# Chapter 2 Question 7
# Write a program that prompts the user to
# enter the minutes (e.g., 1 billion), and displays the number of years and days for
# the minutes. For simplicity, assume a year has 365 days.


def main():
    minutes = eval(input("Enter the number of minutes : "))
    days, years = _calculate_(minutes)
    print(minutes, "minutes is approximately", years, "years and", days, "days.")


def _calculate_(minutes):
    years = minutes / (365 * 24 * 60)
    days = (years - int(years))*365
    return int(days), int(years)


if __name__ == "__main__":
    main()
