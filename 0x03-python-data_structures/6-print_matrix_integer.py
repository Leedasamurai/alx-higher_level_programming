#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i, item in enumerate(row):
            if i < len(row) - 1:
                print("{:d} ".format(item), end="")
            else:
                print("{:d}".format(item))
    if not matrix:
        print("")
