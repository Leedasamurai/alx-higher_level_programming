#!/usr/bin/python3
"""Module for Base class."""
import json
import csv

class Base:
    """A Base class."""
    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor.

        Args:
            id (int): Identifier for the instance with None as def.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Convert a list of dictionaries to a JSON string.

        Args:
            list_dictionaries (list): list of dictionaries.

        Returns:
            str: JSON string representation of list_dictionaries.
        """
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save a list of instances to a file in JSON format.

        Args:
            list_objs (list): list of instances.

        Returns:
            None
        """
        filename = "{}.json".format(cls.__name__)
        with open(filename, "w") as file:
            if list_objs is None:
                file.write("[]")
            else:
                dictionaries = [obj.to_dictionary() for obj in list_objs]
                file.write(cls.to_json_string(dictionaries))

    @staticmethod
    def from_json_string(json_string):
        """Convert a JSON string to a list of dictionaries.

        Args:
            json_string (str): JSON string.

        Returns:
            list: list of dictionaries.
        """
        if json_string is None or not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Create an instance with all attributes already set.

        Args:
            **dictionary: Double pointer to dictionary.

        Returns:
            Instance with all attributes set.
        """
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)
        else:
            dummy_instance = cls()
        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """load list of instances from file in JSON format.

        Returns:
            list: List of instances.
        """
        filename = "{}.json".format(cls.__name__)
        try:
            with open(filename, "r") as file:
                data = file.read()
                dictionaries = cls.from_json_string(data)
                instances = [cls.create(**d) for d in dictionaries]
                return instances
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Save a list of instances to a CSV file.

        Args:
            list_objs (list): List of instances.

        Returns:
            None
        """
        filename = "{}.csv".format(cls.__name__)
        with open(filename, "w", newline='') as file:
            writer = csv.writer(file)
            for obj in list_objs:
                writer.writerow(obj.to_dictionary().values())

    @classmethod
    def load_from_file_csv(cls):
        """Load a list of instances from a CSV file.

        Returns:
            list: List of instances.
        """
        filename = "{}.csv".format(cls.__name__)
        try:
            with open(filename, "r") as file:
                reader = csv.reader(file)
                dictionaries = [cls.to_dictionary_from_csv(row) for row in reader]
                instances = [cls.create(**d) for d in dictionaries]
                return instances
        except FileNotFoundError:
            return []

    @staticmethod
    def to_dictionary_from_csv(row):
        """Convert a CSV row to a dictionary.

        Args:
            row (list): CSV row.

        Returns:
            dict: Dictionary representation of the CSV row.
        """
        return {key: int(value) for key, value in zip(["id", "width", "height", "x", "y"], row)}    
