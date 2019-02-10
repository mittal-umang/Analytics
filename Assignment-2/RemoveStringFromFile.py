def main():
    fileName = input("Enter a FileName: ")
    removeString = input("Enter the string to be removed:")
    with open(fileName, "rt") as fin:
        with open(fileName, "wt") as fout:
            for line in fin:
                try:
                    fout.write(line.replace(removeString, ''))
                except Exception:
                    print("An Error occurred")
                finally:
                    print("Done")

