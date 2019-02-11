# Chapter 13 Question 3
# Write a program that reads the scores from the file and displays their
# total and average. Scores are separated by blanks


def int_string(alist):
    intList = []
    for i in range(len(alist)):
        if alist[i] != '' :
            intList.append(int(alist[i]))
    return intList


def main():
    fileName = input("Enter a FileName: ")
    try:
        with open(fileName, "rt") as fin:
            scores = fin.read().split(" ")
    except FileNotFoundError:
        print("File Not Found")
    except OSError:
        print("Cannot Open File")
    finally:
        fin.close()

    scores = int_string(scores)
    print("There are", len(scores), "scores")
    print("The total is ", sum(scores))
    print("The Average is:", sum(scores) / len(scores))


if __name__ == "__main__":
    main()
