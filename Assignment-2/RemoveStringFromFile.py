# Chapter 13 Question 1
# Write a program that removes all the occurrences of a specified
# string from a text file. Your program should prompt the user to enter a filename
# and a string to be removed.


def main():
    fileName = input("Enter a FileName: ")
    removeString = input("Enter the string to be removed:")
    try:
        with open(fileName, "rt") as fin:
            try:
                newText = fin.read().replace(removeString, '')
            except Exception:
                print("An Error occurred")
            finally:
                fin.close()
                try:
                    with open(fileName, "wt") as fout:
                        fout.write(newText)
                except IOError:
                    print("File Cannot be written")
                finally:
                    fin.close()
    except FileNotFoundError:
        print("File Not Found")
    finally:
        print("Done")


if __name__ == '__main__':
    main()
