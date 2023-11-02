#!/usr/bin/python3

if __name__ == "__main__":

    import sys

    arg = len(sys.argv) - 1

    if arg == 0:
        print("{} arguments.".format(arg))
    elif arg == 1:
        print("{} arguments:".format(arg))
    else:
        print("{} arguments:".format(arg))

    if arg >= 1:
        
        arg = 0

        for args in sys.argv:

            if arg != 0:
                print("{}: {}".format(arg, args))
            arg += 1
# a program that prints the number of and the list of its arguments.
