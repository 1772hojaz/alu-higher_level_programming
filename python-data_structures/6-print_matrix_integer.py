#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i in range(len(row)):
            print("{:d}".format(row[i]), end="")
            if i != len(row) - 1:
                print(" ", end="")
        print()


def new_line():
    print()


def main():
    print_matrix_integer(matrix=[[]])
    new_line()


if __name__ == "__main__":
    main()
