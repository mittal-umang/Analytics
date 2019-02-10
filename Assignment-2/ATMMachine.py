# Chapter 12 Question 3
from AccountClass import Account


def getIndex(alist, id):
    for i in range(len(alist)):
        if alist[0].getId() == id:
            return i
    return -1


def main():
    idList = [Account(id=i, balance=100) for i in range(10)]
    id = eval(input("Enter an account id:"))
    accountIndex = getIndex(idList, id)
    choice = 0
    while choice != 4:
        print("Main menu\n1: Check balance\n2: Withdraw\n3: Deposit\n4: Exit")
        choice = eval(input("Enter a choice: "))
        if choice == 1:
            print("Current Balance is ", idList[accountIndex].getBalance())
        elif choice == 2:
            try:
                idList[accountIndex].withdraw(eval(input("Enter an amount to withdraw: ")))
            except Exception as error:
                print(error)
        elif choice == 3:
            idList[accountIndex].deposit(eval(input("Enter an amount to deposit: ")))


if __name__ == "__main__":
    main()
