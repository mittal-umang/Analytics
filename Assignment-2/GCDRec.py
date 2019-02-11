# Chapter 15 Question 3
# Write a recursive function to find the GCD. Write a test program that prompts the
# user to enter two integers and displays their GCD.

def gcd(m, n):
    if m % n == 0:
        return n
    else:
        return gcd(n, m % n)


def main():
    a, b = eval(input("Enter numbers: "))
    print("GCD is", gcd(a, b))


if __name__ == "__main__":
    main()
