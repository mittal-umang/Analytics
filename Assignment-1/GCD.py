# Chapter 5 Question 16
# Compute the greatest common divisor


def __main__():
    num1, num2 = eval(input("Enter two number with comma : "))
    if num1 > num2:
        d = num2
    else:
        d = num1

    while d > 0:
        if num1 % d == 0 and num2 % d == 0:
            break
        d -= 1

    print("The Greatest Common Divisor of ", num1, "and", num2, "is", d)


__main__()
