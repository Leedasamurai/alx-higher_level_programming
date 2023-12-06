#!/usr/bin/python3
"""
Module documentation goes here.
"""

def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure for JSON serialization of an object.

    Args:
        obj: An instance of a Class with serializable attributes.

    Returns:
        dict: The dictionary description for JSON serialization.
    """
    json_dict = {}
    for key, value in obj.__dict__.items():
        if isinstance(value, (int, bool, str, list, dict)):
            json_dict[key] = value
    return json_dict
