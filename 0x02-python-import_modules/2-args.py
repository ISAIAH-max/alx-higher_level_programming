#!/usr/bin/python3
import sys
if __name__ == "__main__":
    x = len(sys.argv) - 1
    if x == 0:
        print("{} arguments.".format(x))
    else:
        print("{} arguments:".format(x))
        for y in range(x):
            print("{}: {}".format(y+1, sys.argv[y+1]))
