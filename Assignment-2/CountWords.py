# Chapter 13 Question 6
# Write a program that counts the number of words in President
# Abraham Lincoln’s Gettysburg Address

# changed the address since address was not available

import urllib.request
import re


def main():
    url = "https://www.d.umn.edu/~rmaclin/gettysburg-address.html".strip()
    infile = urllib.request.urlopen(url)
    regex = re.compile('<.*?>')
    s = re.sub(regex, '', infile.read().decode())
    print("There are", countLetters(s.lower()), "characters in the address")


def countLetters(s):
    counts = 0
    for ch in s:
        if ch.isalpha():
            counts += 1
    return counts


if __name__ == '__main__':
    main()
