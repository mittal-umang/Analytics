# Chapter 10 Question 26
# Write the following function that merges two sorted lists
# into a new sorted list


def merge(list1, list2):
    list3 = []
    while list1 and list2:
        if list1[len(list1) - 1] > list2[len(list2) - 1]:
            list3.append(list1.pop())
        else:
            list3.append(list2.pop())

    return (list3 + list2 + list1)[::-1]


def main():
    print("Enter First list of numbers : ")
    list1 = [int(x) for x in input().split()]
    print("Enter Second list of numbers : ")
    list2 = [int(x) for x in input().split()]

    print(merge(list1, list2))


if __name__ == "__main__":
    main()
