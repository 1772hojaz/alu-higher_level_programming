#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return
    for i in reversed(my_list):
        print("{:d}".format(i))


def main():
    print_reversed_list_integer(my_list=[])


if __name__ == "__main__":
    main()
