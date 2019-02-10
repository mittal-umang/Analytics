# Chapter 10 Question 3
# Write a program that reads some integers
# between 1 and 100 and counts the occurrences of each.

def bubble_sort(alist):
    for i, num in enumerate(alist):
        try:
            if alist[i + 1] < num:
                alist[i] = alist[i + 1]
                alist[i + 1] = num
                bubble_sort(alist)
        except IndexError:
            pass


def occurenceMap(alist):
    i = 0
    occurenceMap = {}
    bubble_sort(alist)
    while i < len(alist):
        count = alist.count(alist[i])
        occurenceMap.update({alist[i]: count})
        i += 1
    return occurenceMap


def main():
    print("Enter a list of numbers : ")
    numberList = [int(x) for x in input().split()]
    map = occurenceMap(numberList)
    for k in map:
        if map.get(k) > 1:
            map.update({k: str(map.get(k)) + " times"})
        else:
            map.update({k: str(map.get(k)) + " time"})
        print(str(k), "occurs", map.get(k))


if __name__ == "__main__":
    main()
