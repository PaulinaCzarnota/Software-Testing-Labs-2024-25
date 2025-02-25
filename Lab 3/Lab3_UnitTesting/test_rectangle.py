"""
Unit tests for the Rectangle class.
"""
import unittest
from rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.rect = Rectangle(10, 5)

    def test_initialization(self):
        self.assertEqual(self.rect.get_length(), 10)
        self.assertEqual(self.rect.get_width(), 5)
        self.assertEqual(self.rect.get_area(), 50)

    def test_set_length(self):
        self.rect.set_length(8)
        self.assertEqual(self.rect.get_length(), 8)

    def test_rotate(self):
        self.rect.rotate()
        self.assertEqual(self.rect.get_length(), 5)
        self.assertEqual(self.rect.get_width(), 10)

if __name__ == "__main__":
    unittest.main()