import unittest
import json
from models.base import Base  # Adjust the import based on your actual project structure

class TestBase(unittest.TestCase):

    def test_constructor_with_id(self):
        instance = Base(42)
        self.assertEqual(instance.id, 42)

    def test_constructor_without_id(self):
        instance1 = Base()
        instance2 = Base()
        self.assertEqual(instance1.id, 1)
        self.assertEqual(instance2.id, 2)

    def test_to_json_string_empty_list(self):
        result = Base.to_json_string([])
        self.assertEqual(result, "[]")

    def test_to_json_string_non_empty_list(self):
        data = [{"key": "value"}, {"key2": "value2"}]
        result = Base.to_json_string(data)
        expected_result = json.dumps(data)
        self.assertEqual(result, expected_result)

    def test_save_to_file_with_list_objs_none(self):
        Base.save_to_file(None)
        with open("Base.json", "r") as file:
            result = file.read()
        self.assertEqual(result, "[]")

    def test_save_to_file_with_list_objs_non_empty(self):
        # Assuming you have a class with a to_dictionary method
        class MockObj:
            def to_dictionary(self):
                return {"key": "value"}

        list_objs = [MockObj(), MockObj(), MockObj()]
        Base.save_to_file(list_objs)
        with open("Base.json", "r") as file:
            result = file.read()
        expected_result = Base.to_json_string([obj.to_dictionary() for obj in list_objs])
        self.assertEqual(result, expected_result)

    def test_from_json_string_empty_string(self):
        result = Base.from_json_string("")
        self.assertEqual(result, [])

    def test_from_json_string_non_empty_string(self):
        data = '[{"key": "value"}, {"key2": "value2"}]'
        result = Base.from_json_string(data)
        expected_result = json.loads(data)
        self.assertEqual(result, expected_result)

    def test_create_rectangle(self):
        # Assuming you have a Rectangle class with an update method
        class MockRectangle:
            def __init__(self, width, height):
                self.width = width
                self.height = height
            def update(self, **kwargs):
                self.__dict__.update(kwargs)

        result = Base.create(Rectangle=MockRectangle, width=10, height=20)
        self.assertIsInstance(result, MockRectangle)
        self.assertEqual(result.width, 10)
        self.assertEqual(result.height, 20)

    def test_create_square(self):
        # Assuming you have a Square class with an update method
        class MockSquare:
            def __init__(self, size):
                self.size = size
            def update(self, **kwargs):
                self.__dict__.update(kwargs)

        result = Base.create(Square=MockSquare, size=5)
        self.assertIsInstance(result, MockSquare)
        self.assertEqual(result.size, 5)

    def test_load_from_file_file_not_found(self):
        result = Base.load_from_file()
        self.assertEqual(result, [])

    # Add more test cases as needed

if __name__ == '__main__':
    unittest.main()

