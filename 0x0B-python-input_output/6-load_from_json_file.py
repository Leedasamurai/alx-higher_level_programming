#!/usr/bin/python3
"""
Module documentation goes here.
"""

import json

def load_from_json_file(filename):
    """
    Creates an Object from a “JSON file”.

    Args:
        filename (str): The name of the JSON file.

    Returns:
        obj: The Python data structure represented by the JSON file.
    """
    with open(filename, mode="r", encoding="utf-8") as file:
        return json.load(file)
