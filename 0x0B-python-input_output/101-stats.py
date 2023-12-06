#!/usr/bin/python3
"""
Log parsing
"""

import sys

def print_metrics(total_size, status_codes):
    """
    Prints the computed metrics.

    Args:
        total_size (int): The total file size.
        status_codes (dict): A dictionary containing the count of each status code.
    """
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))
