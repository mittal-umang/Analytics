# Chapter 5 Question 11
# Write a program that prompts the user to enter the
# number of students and each student’s score, and displays the highest and secondhighest
# scores.


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
    noOfStudents = eval(input("Enter the number of students: "))
    i = 1
    list = []
    while i < noOfStudents + 1:
        list.append(int(input("Enter the score of student " + str(i) + " : ")))
        i += 1
    bubble_sort(list)
    list.reverse()
    print("The highest score is ", list[0], "and second highest score is", list[1])


if __name__ == "__main__":
    main()
