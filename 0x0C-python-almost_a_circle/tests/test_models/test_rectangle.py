#!/usr/bin/python3
'''Module for Rectangle unit tests.'''

import unittest
from models.rectangle import Rectangle
import io

class TestRectangle(unittest.TestCase):
    """Test cases for the Rectangle class."""

    def test_rectangle_constructor(self):
        """Test constructor with default id."""
        r = Rectangle(5, 10)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_rectangle_constructor_with_id(self):
        """Test constructor with specified id."""
        r = Rectangle(3, 7, 2, 4, 42)
        self.assertEqual(r.id, 42)
        self.assertEqual(r.width, 3)
        self.assertEqual(r.height, 7)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 4)

    def test_rectangle_area(self):
        """Test area method."""
        r = Rectangle(4, 6)
        self.assertEqual(r.area(), 24)

    def test_rectangle_display(self):
        """Test display method."""
        r = Rectangle(2, 3)
        expected_output = "##\n##\n##\n"
        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            r.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()
