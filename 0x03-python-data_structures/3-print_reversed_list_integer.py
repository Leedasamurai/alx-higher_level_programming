#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list:
        if len(my_list) > 0:
            i = len(my_list) - 1
            for m in my_list:
                print("{}".format(my_list[i]))
                i -= 1
# Write a function that prints all integers of a list, in reverse order.
