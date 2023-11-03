#!/usr/bin/python3
import sys

if __name__ == "__main__":
    
    argu = sys.argv[1:]
    add = 0

    for arg in argu:
        add += int(arg)

    print(add)
