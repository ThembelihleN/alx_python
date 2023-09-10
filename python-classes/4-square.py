"""
Classes and objects are the two main aspects of object oriented programming. A class creates a new type where objects are instances of the class
"""
class Square:
    """
    A class is a blueprint or a template for creating objects (instances)
    """ 
    def __init__(self, size = 0):
        self.__size

    @property
    def size(self):
        return self.__sizeof__
    
    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        return self.size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            print("\n")
