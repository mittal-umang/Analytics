# Chapter 8 Question 13


def commonprefix(s1, s2):
    for i, c in enumerate(s1):
        if c != s1[i]:
            return s2[:i]
    return s2


def main():
    s1 = input("Enter First String:")
    s2 = input("Enter Second String:")
    print("longest Common Prefix is", commonprefix(s1, s2))


if __name__ == "__main__":
    main()
