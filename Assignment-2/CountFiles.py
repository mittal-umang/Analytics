# Chapter 15 Question 24
# Write a program that prompts the user to enter a
# directory and displays the number of files in the directory.
import os


def fileCount(folder):
    count = 0

    for filename in os.listdir(folder):
        path = os.path.join(folder, filename)
        if os.path.isfile(path):
            count += 1
    return count


def main():
    directory = input("Enter path: ")
    print("There are ", fileCount(directory), "files")


if __name__ == "__main__":
    main()
