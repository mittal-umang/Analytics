# Chapter 13 Question 2
# Write a program that will count the
# number of characters, words, and lines in a file. Words are separated by a whitespace
# character. Your program should prompt the user to enter a filename


def main():
    fileName = input("Enter a FileName: ")
    try:
        with open(fileName, "rt") as fin:
            fileContents = fin.read()
    except FileNotFoundError:
        print("File Not Found")
    except OSError:
        print("Cannot Open File")
    finally:
        fin.close()

    print(len(fileContents), " Characters")
    print(len(fileContents.split(" ")), " Words")
    print(len(fileContents.split()), " Lines")


if __name__ == "__main__":
    main()
