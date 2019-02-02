# Chapter 3 Question 9
# Write a program that reads the following information
# and prints a payroll statement:
# Employee’s name
# Number of hours worked in a week
# Hourly pay rate
# Federal tax withholding rate
# State tax withholding rate


def __calculations__(hours, hourlypay, federalrate, staterate):
    return hours * hourlypay, hours * hourlypay * federalrate, hours * hourlypay * staterate


def main():
    name = input("Enter employee's name: ")
    hours = eval(input("Enter number of hours worked in a week: "))
    hourlyRate = float(input("Enter hourly pay rate: "))
    federalRate = float(input("Enter federal tax withholding rate: "))
    stateRate = float(input("Enter state tax withholding rate: "))
    grossPay, federalTax, stateTax = __calculations__(hours, hourlyRate, federalRate, stateRate)
    deductions = federalTax + stateTax
    netPay = grossPay - deductions

    print("Employee Name:", name)
    print("Hours Worked:", '%.1f' % hours)
    print("Pay Rate: $", '%.2f' % hourlyRate, sep="")
    print("Gross Pay: $", '%.1f' % grossPay, sep="")
    print("Deductions:")
    print("\tFederal Withholding (", federalRate * 100, "%): $", federalTax, sep="")
    print("\tState Withholding (", stateRate * 100, "%): $", stateTax, sep="")
    print("\tTotal Deduction: $", deductions, sep="")
    print("Net Pay: $", '%.2f' % netPay, sep="")


main()
