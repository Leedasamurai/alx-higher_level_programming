#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None

    mx_value = my_list[0]
    for i in my_list:
        if i > mx_value:
            mx_value = i

    return mx_value
