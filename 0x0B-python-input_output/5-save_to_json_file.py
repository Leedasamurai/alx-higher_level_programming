#!/usr/bin/python3
"""
Module documentation goes here.
"""

import json

def save_to_json_file(my_obj, filename):
    """
    Writes an Object to a text file, using a JSON representation.

    Args:
        my_obj: The object to be serialized to JSON.
        filename (str): The name of the file to write the JSON representation.

    Returns:
        None
    """
    with open(filename, mode="w", encoding="utf-8") as file:
        json.dump(my_obj, file)
