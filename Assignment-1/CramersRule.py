# Chapter 4 Question 3
# (Algebra: solve linear equations in two variables) You can use Cramer’s rule to solve the
# system of linear equation.
# Write a program that prompts the user to enter a, b, c, d, e, and f and display the
# result.


def __cramerRule__(a, b, c, d, e, f):
    deno = a * d - b * c
    numerx = e * d - b * f
    numery = a * f - e * c
    if deno == 0:
        return None, None
    else:
        x = numerx / deno
        y = numery / deno
        return x, y


def main():
    a, b, c, d, e, f = eval(input("Enter a, b, c, d, e, f: "))
    x, y = __cramerRule__(a, b, c, d, e, f)
    if x is None and y is None:
        print("The equation has no solution.")
    else:
        print("x is ", x, "and y is", y)


if __name__ == "__main__":
    main()
