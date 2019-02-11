# Chapter 15 Question 23
# Write a recursive function to print all the permutations of a
# string.

def displayPermuation(s):
    return displayPermuationHelper(" ", list(s))


def displayPermuationHelper(s1, s2):
    if len(s2) == 0:
        return s1
    else:
        for i in range(len(s2)):
            return displayPermuationHelper(s2.pop(), s2)


print(displayPermuation("abc"))
