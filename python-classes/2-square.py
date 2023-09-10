"""
Classes and objects are the two main aspects of object oriented programming. A class creates a new type where objects are instances of the class.
""" 
class Square:
    """
    A class is a blueprint or a template for creating objects (instances)
    """
    def __init__(self, size = 0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return self.__size * self.__size