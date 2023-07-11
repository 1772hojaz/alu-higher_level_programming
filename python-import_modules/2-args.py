#!/usr/bin/python3


import sys


def main():
    args = sys.argv[1:]
    num_args = len(args)
    if num_args == 1:
        print("1 argument:")
    else:
        print("{} argument{}:".format(num_args, "s" if num_args != 1 else ""))
    for i, arg in enumerate(args, start=1):
        print("{}: {}".format(i, arg))


if __name__ == "__main__":
    main()
