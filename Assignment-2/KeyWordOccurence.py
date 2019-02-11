# Chapter 14 Question 3
# Write a program that reads in a Python
# source code file and counts the occurrence of each keyword in the file. Your program
# should prompt the user to enter the Python source code filename.

def main():
    keyWords = {"and": 0, "as": 0, "assert": 0, "break": 0, "class": 0,
                "continue": 0, "def": 0, "del": 0, "elif": 0, "else": 0,
                "except": 0, "False": 0, "finally": 0, "for": 0, "from": 0,
                "global": 0, "if": 0, "import": 0, "in": 0, "is": 0, "lambda": 0,
                "None": 0, "nonlocal": 0, "not": 0, "or": 0, "pass": 0, "raise": 0,
                "return": 0, "True": 0, "try": 0, "while": 0, "with": 0, "yield": 0}

    filename = input("Enter a Python source code filename: ").strip()

    try:
        with open(filename) as fin:
            text = fin.read().split()
    except FileNotFoundError:
        print("File Not Found")
    finally:
        fin.close()

    keys = list(keyWords.keys())
    for word in text:
        if word in keys:
            keyWords[word] += 1

    for i in range(len(keys)):
        if keyWords.get(keys[i]) < 1:
            print(keys[i], "occurs", keyWords.get(keys[i]), "time")
        else:
            print(keys[i], "occurs", keyWords.get(keys[i]), "times")


if __name__ == "__main__":
    main()
