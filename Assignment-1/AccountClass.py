class Account:
    def __init__(self, id=0, balance=100, annualinterestrate=0):
        self.__id = id
        self.__balance = balance
        self.__annualInterestRate = annualinterestrate

    def getMonthlyInterestRate(self):
        return str(self.__annualInterestRate * 100) + "%"

    def getMonthlyInterest(self):
        return "$" + str(self.__annualInterestRate * self.__balance / 12)

    def getId(self):
        return self.__id

    def getBalance(self):
        return "$" + str(self.__balance)

    def withdraw(self, amount):
        self.__balance -= amount

    def deposit(self, amount):
        self.__balance += amount


def main():
    account = Account(1122, 20000, 0.045)
    print("Current account balance is ", account.getBalance())
    account.withdraw(2500)
    print("Account balance after withdrawal is  ", account.getBalance())
    account.deposit(3000)
    print("Account balance after deposit is ", account.getBalance())
    print("Account Details are as below: ")
    print("\tAccount ID : ", account.getId())
    print("\tCurrent Balance is ", account.getBalance())
    print("\tAnnual Interest rate is ", account.getMonthlyInterestRate())
    print("\tAnnual Interest is ", account.getMonthlyInterest())


if __name__ == "__main__":
    main()
