# Chapter 5 Question 9
# Suppose that the tuition for a university
# is $10,000 this year and increases 5% every year. Write a program that
# computes the tuition in ten years and the total cost of four years’ worth of tuition
# starting ten years from now.


def __increment__(number):
    return number + number * 0.05


def main():
    currentTuition = eval(input("Enter Current Tuition: "))
    year = 1
    while year < 15:
        currentTuition = __increment__(currentTuition)
        if year == 10:
            tuitionYear10 = currentTuition
        elif year == 14:
            tuitionYear14 = currentTuition
        else:
            pass
        year += 1

    print("Tuition after 10 years from now : ", tuitionYear10)
    print("Tuition after 14 years from now : ", tuitionYear14)


if __name__ == "__main__":
    main()
