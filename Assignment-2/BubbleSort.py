# Chapter 10 Question 16
# Bubble Sort


def bubble_sort(alist):
    for i, num in enumerate(alist):
        try:
            if alist[i + 1] < num:
                alist[i] = alist[i + 1]
                alist[i + 1] = num
                bubble_sort(alist)
        except IndexError:
            pass


def main():
    print("Enter List of numbers : ")
    numberList = [int(x) for x in input().split()]
    print("Sort list is:")
    bubble_sort(numberList)
    print(numberList)


if __name__ == "__main__":
    main()
