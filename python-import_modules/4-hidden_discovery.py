#!/usr/bin/python3


#humphrey
if __name__ == "__main__":
    import hidden_4
    import sys

    for n in dir(hidden_4):
        if n[:2] != "__":
            print(n)
