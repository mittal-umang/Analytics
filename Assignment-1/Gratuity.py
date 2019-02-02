# Chapter 2 Question 5
# (Financial application: calculate tips) Write a program that reads the subtotal and
# the gratuity rate and computes the gratuity and total. For example, if the user
# enters 10 for the subtotal and 15% for the gratuity rate, the program displays 1.5
# as the gratuity and 11.5 as the total.


def main():
    subTotal, gratuity = eval(input("Enter sub-total and gratuity : "))
    gratuityAmount, total = _calculateGratuity_(gratuity, subTotal)
    print("The gratuity is", '%.2f' % gratuityAmount, "and the total is", '%.2f' % total)


def _calculateGratuity_(gratuity, subTotal):
    gratuityAmount = subTotal * gratuity / 100
    total = subTotal + gratuityAmount
    return gratuityAmount, total


main()
