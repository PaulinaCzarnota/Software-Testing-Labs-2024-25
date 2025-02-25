"""
This module defines the Rectangle class.
Includes fixes for:
- Typo in "self.lenght" (changed to "self.length").
- Incorrect rotation logic (swapping length and width correctly).
- Area update bug when setting width/length.
"""

class Rectangle:
    def __init__(self, length=None, width=None):
        """Initialize a rectangle with length and width."""
        self.length = length
        self.width = width
        if length is not None and width is not None:
            self.area = length * width
            self.is_square = length == width

    def set_length(self, length):
        """Set length and update area."""
        self.length = length
        self.area = self.length * self.width
        self.is_square = self.length == self.width

    def set_width(self, width):
        """Set width and update area."""
        self.width = width
        self.area = self.length * self.width
        self.is_square = self.length == self.width

    def reset(self):
        """Reset rectangle attributes."""
        self.length = 0
        self.width = 0
        self.area = 0

    def get_area(self):
        """Return the area of the rectangle."""
        return self.area

    def get_length(self):
        """Return length."""
        return self.length

    def get_width(self):
        """Return width."""
        return self.width

    def get_is_square(self):
        """Check if the rectangle is a square."""
        return self.is_square

    def rotate(self):
        """Swap length and width."""
        self.length, self.width = self.width, self.length