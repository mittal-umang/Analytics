# Chapter 5 Question 19
# Write a program that prompts the user to enter an integer
# from 1 to 15 and displays a pyramid

def main():
    level = eval(input("Enter the level of the triangle "))
    __Pattern__(level)


def __Pattern__(level):
    for i in range(0, level):
        for j in range(level - i, 1, -1):
            print(" ", end="\t")
        for j in range(i + 1, 0, -1):
            print(j, end="\t", sep="\t")
        for j in range(1, i + 1):
            print(j + 1, end="\t", sep="\t")
        print("\n")


if __name__ == "__main__":
    main()
