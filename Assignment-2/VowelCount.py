# Chapter 14 Question 11
# Write a program that prompts the user to enter a
# text filename and displays the number of vowels and consonants in the file. Use
# a set to store the vowels A, E, I, O, and U.


def main():
    vowels = ('a', 'e', 'i', 'o', 'u')
    fileName = input("Enter a FileName: ")
    vowelCount = 0
    consonantsCount = 0
    try:
        with open(fileName, "rt") as fin:
            fileContents = fin.read().split(" ")
    except FileNotFoundError:
        print("File Not Found")
    except OSError:
        print("Cannot Open File")
    finally:
        fin.close()

    while fileContents:
        word = fileContents.pop().lower()
        for i in word:
            if i.isalpha():
                if i in vowels:
                    vowelCount += 1
                else:
                    consonantsCount += 1

    print("There are ", vowelCount, "vowels and", consonantsCount, "consonants in", fileName)


if __name__ == "__main__":
    main()
