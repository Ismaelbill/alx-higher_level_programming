#!/usr/bin/python3
"""Square module"""


class Square:
    """Defines a sqaure"""

    def __init__(self, size=0):
        """Constructor.

        Args:
            size: length of a side of the square

        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Area of this square

        Returns:
            the size squared
        """
        return self.__size ** 2
