"""
Write a program to print the following pattern
A
B C D
E F G H I
J K L M N O P
Q R S T U V W X
"""


def pattern():
    chars = [chr(x) for x in range(ord('A'), ord('Z'))]
    limit = 1
    i = 0
    for char in chars:
        i += 1
        print(char, end=" ")
        if (limit == i):
            print()
            limit += 2
            i = 0


pattern()
