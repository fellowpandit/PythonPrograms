""" Write a Python program to read a string of 4 characters from the user. 
    Convert every character in the strin gto its next alphabet.           """

# Using built in methods


def changeChar(string):
    result = ""
    for char in string:
        if (char == 'z'):
            char = chr(ord('a')-1)
        result += chr(ord(char)+1)

    return result


# Doesn't use built-in methods
def changeCharr(string):
    result = ""
    chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
             'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    length = len(chars)
    for char in string:
        for i in range(length):
            if (char == chars[i]):
                x = (i+1) % length
                result += chars[x]

    return result


def main():
    string = input("Enter the string:")[0:4]
    print(changeCharr(string))


main()
