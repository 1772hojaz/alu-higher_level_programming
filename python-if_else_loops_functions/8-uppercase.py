#!/usr/bin/python3
# For uppercase


def uppercase(str):
    for char in str:
        if ord(char) >= 97 and ord(char) <= 122:
            char = chr(ord(char) - 32)
        print(char, end="")
    print()
